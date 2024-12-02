from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Device, Detector

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['detector', 'name']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class DetectorForm(forms.ModelForm):
    class Meta:
        model = Detector
        fields = ['active', 'name', 'group', 'location', 'data_source', 'set_dose_rate', 'set_threshold', 'set_noise', 'total_dose', 'dose_rate', 'cps']

    def __init__(self, *args, **kwargs):
        super(DetectorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        # Bulma form classes
        self.helper.form_class = 'form'  # General form styling
        self.helper.label_class = 'label'  # Label styling
        self.helper.field_class = 'control'  # Input field styling
        self.helper.form_show_labels = True

        # Optional: Add specific Bulma classes for elements such as buttons and inputs
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})  # Bulma input class for text fields
        
        # Pokud je to boolean pole, použijeme 'checkbox' widget
        self.fields['set_noise'].widget = forms.CheckboxInput(attrs={'class': 'checkbox'})
        self.fields['active'].widget = forms.CheckboxInput(attrs={'class': 'checkbox'})
        self.fields['group'].disabled = True
        self.fields['location'].disabled = True
        self.fields['data_source'].disabled = True
        self.fields['dose_rate'].disabled = True
        self.fields['cps'].disabled = True


        # Adding the submit button
        self.helper.add_input(Submit('submit', 'Save', css_class='button is-primary'))
