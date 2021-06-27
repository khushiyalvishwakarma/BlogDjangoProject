from django import forms
from .models import bloglistmdl

class bloglist_form(forms.ModelForm):
    class Meta:
        model=bloglistmdl
        fields='__all__'


