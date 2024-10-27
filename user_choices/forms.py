# forms.py
from django import forms
from .models import UserChoice

class NotesForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={
                'rows': 4,
                'class': 'border border-gray-300 rounded-md p-2 w-full',  # Add Tailwind CSS classes here
                'placeholder': 'Enter your notes here...'  # Optional placeholder text
            })
        }
