from django import forms
from django.core import validators
class ContactForm(forms.Form):
    name = forms.CharField(label='UserName', initial='Apurba', help_text='Total lenght must be less than 60 characters', required=False, widget=forms.Textarea)
    # file = forms.FileField()
    # email = forms.EmailField(label='UserEmail')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    check = forms.BooleanField(label='Available')
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'),('M', 'Mashroom'), ('C', 'Chicken')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if 'gmail.com' not in valemail:
    #         raise forms.ValidationError("Email must contain @gmail.com at the end")
        
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Name must be at least 10 characters")


class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message="Name must be at least 10 characters")])
    email = forms.CharField(validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35, message="Age must be under 35"), validators.MinValueValidator(20, message="Age must be at least 20")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='allowed only png and pdf')])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['name']
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['confirm_password']

        if pass1 != pass2:
            raise forms.ValidationError("Password didn't match")
        if len(username) > 10:
            raise forms.ValidationError("Name must be less than 10 characters")