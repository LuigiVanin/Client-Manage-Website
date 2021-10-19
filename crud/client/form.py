from django.forms import ModelForm, fields
from .models import Clients

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
            'surname',
            'email',
            'age',
            'debt'
        ]
    