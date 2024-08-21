from django import forms
from .models import Attachments

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ('file',)
