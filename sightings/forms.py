from django.forms import ModelForm

from .models import Squirrel


class UpdateRequestForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = [
            'longitude',
            'latitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age'
        ]



