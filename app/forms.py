from django import forms
from .models import Index

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['first_name', 'last_name', 'phone_number', 'photos']