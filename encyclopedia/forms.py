from turtle import width
from django import forms

from encyclopedia.util import get_entry
from django.core.exceptions import ValidationError


class EntryForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    def clean(self):
        title = self.cleaned_data['title']
        if get_entry(title) is not None:
            raise ValidationError('The Entry has already been created!')
        return self.cleaned_data