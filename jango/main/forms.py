from .models import impytADMIN
from django.forms import ModelForm, TextInput

class impytADMINForm(ModelForm):
    class Meta:
        model = impytADMIN
        fields = ['title']
        

        widgets = {
            "title": TextInput(attrs={
            'class': 'formControl',
            'placeholder': 'Васап введи текст',
            })
        }