from .models import Person
from django import forms


class GreetingForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
