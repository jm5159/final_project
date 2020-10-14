from django.forms import ModelForm

from .models import AdoptRequest


class AdoptRequestForm(ModelForm):
    class Meta:
        model = AdoptRequest
        # All other fields are handled in the background
        fields = [
            'longitude',
            'latitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age'
        ]
