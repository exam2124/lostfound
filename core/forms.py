# core/forms.py

from django import forms
from .models import Item

class ItemReportForm(forms.ModelForm):
    """Used for both Lost and Found item reporting"""

    class Meta:
        model = Item
        # We exclude user and item_type — those are set in the view
        fields = ['item_name', 'description', 'location', 'date_time', 'contact_info', 'image']

        widgets = {
            # Date/time picker in the browser
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'item_name': 'Item Name',
            'description': 'Description',
            'location': 'Where was it lost/found?',
            'date_time': 'Date & Time',
            'contact_info': 'Contact Info (optional)',
            'image': 'Upload Image (optional)',
        }