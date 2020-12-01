from django import forms
from app1.models import Customer,productmodel

class Custerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class Productform(forms.ModelForm):
    class Meta:
        model = productmodel
        fields = "__all__"
