from django import forms

from .models import ADDRESS

class AddressForm(forms.ModelForm):
    class Meta:
        model = ADDRESS
        fields = [
            #'billing_profile',
            #'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code'
        ]