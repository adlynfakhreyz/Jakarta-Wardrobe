from django import forms
from .models import Forum, Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description', 'purpose']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm',
                'placeholder': 'Got something to say? Start here! (max 50 characters)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm',
                'placeholder': 'Write your post here...'
            }),
            'purpose': forms.Select(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm',
            }),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 75:
            raise forms.ValidationError("Title cannot exceed 75 characters.")
        return title
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Add your comment...',
                'rows': 3,  # mengatur tinggi menjadi lebih kecil
                'cols': 50,  # opsional, untuk mengatur lebar
            }),
        }

