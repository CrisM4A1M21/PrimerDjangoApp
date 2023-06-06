from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        # solo usar para formularios personalizados como este
        # widgets permite agregar clases de css o boostrap
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'})
        }