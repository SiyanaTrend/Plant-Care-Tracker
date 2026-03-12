from gardeners.models import Gardener


def get_profile():
    return Gardener.objects.first()
