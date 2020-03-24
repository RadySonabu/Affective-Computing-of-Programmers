from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            "description",
            "document",
        )
        labels = {
            "document": "SELECT CSV FILE",
            "description": "Input the student number",
        }
        widgets = {"document": forms.FileInput(attrs={"accept": ".csv"})}
