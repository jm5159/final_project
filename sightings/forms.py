from django.forms import ModelForm

from .models import Squirrel


class UpdateRequestForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = '__all__'
        labels = {"unique_squirrel_id": "Unique_squirrel_id[Hectare-Shift-Date(%m%d)-Squirrel Number]"}
