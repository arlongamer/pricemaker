from django import forms
from .models import PriceEntry

class PriceEntryForm(forms.ModelForm):
    class Meta:
        model = PriceEntry
        fields = ['isin', 'quotation_date', 'price', 'currency', 'source', 'entered_by']
        widgets = {
            'quotation_date': forms.DateInput(attrs={'type': 'date'}),
        }
