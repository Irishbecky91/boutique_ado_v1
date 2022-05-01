from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as __str__


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ('Remove')
    initial_text = ('Current Image')
    input_text = ('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'