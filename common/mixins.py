from common.utils import get_profile


class SingleProfileMixin:
    def get_object(self, queryset=None):
        return get_profile()


class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


class HiddenHelpText:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = ''
