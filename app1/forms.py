from django import forms
from .models import *

class regForm(forms.ModelForm):
    class Meta:
        model=Regmodel
        fields='__all__'