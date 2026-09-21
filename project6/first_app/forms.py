from django import forms
from first_app.models import student
class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'