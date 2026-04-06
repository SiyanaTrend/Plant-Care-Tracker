import asyncio
import sys
import threading
from asgiref.sync import sync_to_async
from rest_framework import generics, permissions, filters
from maintenance.serializers import MaintenanceRecordSerializer
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from maintenance.forms import MaintenanceCreateForm, MaintenanceEditForm, MaintenanceDeleteForm
from maintenance.models import MaintenanceRecord
from notifications.services import update_notifications
from plants.models import Plant
from notifications.models import Notification


class MaintenanceDetailsView(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = 'maintenance/maintenance-details.html'
    slug_url_kwarg = 'plant_slug'
    context_object_name = 'plant'

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_notifications(self.request.user)
        return context


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceCreateForm
    template_name = 'maintenance/create-maintenance.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        plant = get_object_or_404(Plant, slug=self.kwargs['plant_slug'], user=self.request.user)
        kwargs['instance'] = MaintenanceRecord(plant=plant)
        return kwargs

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.kwargs['plant_slug']})

    def form_valid(self, form):
        response = super().form_valid(form)
        run_async_maintenance(task_clear_notifications_after_care(self.object.plant.id, self.object.action))
        return response


class MaintenanceEditView(LoginRequiredMixin, UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceEditForm
    template_name = 'maintenance/edit-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(plant__user=self.request.user)

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.object.plant.slug})

    def form_valid(self, form):
        response = super().form_valid(form)
        run_async_maintenance(task_clear_notifications_after_care(self.object.plant.id, self.object.action))
        return response


class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    model = MaintenanceRecord
    form_class = MaintenanceDeleteForm
    template_name = 'maintenance/delete-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(plant__user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.object.plant.slug})


def run_async_maintenance(coro):
    if 'test' in sys.argv:
        return

    def start_loop(loop, coro):
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(coro)
        finally:
            loop.close()

    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(new_loop, coro), daemon=True)
    t.start()


async def task_clear_notifications_after_care(plant_id, action_type):
    if 'test' not in sys.argv:
        await asyncio.sleep(1)

    @sync_to_async
    def clear_alerts():
        deleted_count, _ = Notification.objects.filter(
            plant_id=plant_id,
            action_type=action_type,
        ).delete()
        if deleted_count > 0:
            print(f"--- ASYNC: Cleared {deleted_count} pending alerts for {action_type} on plant {plant_id} ---")
        else:
            print(f"--- ASYNC: No pending alerts found for {action_type} on plant {plant_id} ---")

    await clear_alerts()


class MaintenanceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['action', 'date', 'plant__plant_name']
    ordering_fields = ['id', 'plant__plant_name', 'date']
    ordering = ['-id']

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(plant__user=self.request.user).select_related('plant')

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        if hasattr(serializer, 'fields') and 'plant' in serializer.fields:
            serializer.fields['plant'].queryset = Plant.objects.filter(user=self.request.user)
        return serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        run_async_maintenance(task_clear_notifications_after_care(instance.plant.id, instance.action))


class MaintenanceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(plant__user=self.request.user).select_related('plant')

    def perform_update(self, serializer):
        instance = serializer.save()
        run_async_maintenance(task_clear_notifications_after_care(instance.plant.id, instance.action))
