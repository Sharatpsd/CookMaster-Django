
from django import forms
from .models import Student   # Student Model টা import করতে ভুলিস না

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
