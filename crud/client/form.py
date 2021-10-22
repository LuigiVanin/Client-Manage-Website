from django.forms import ModelForm, fields, widgets
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
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder': 'Primeiro nome do cliente'}),
            'surname': widgets.TextInput(attrs={'placeholder': 'Segundo nome do cliente'}),
            'email': widgets.TextInput(attrs={'placeholder': 'your_email@adrss.com'}),
            'age': widgets.TextInput(attrs={'placeholder': 'Idade do cliente'}),
            'debt': widgets.TextInput(attrs={'placeholder': 'Dívida de seu cliente'}),
        }
        