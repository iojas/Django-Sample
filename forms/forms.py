from django import forms

#from .models import user

from django.contrib.auth.models import User

class userLogin (forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        }
    ))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))





class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    username = forms.RegexField(
        label='Username',
        max_length=30,
        regex=r'^[\w-]+$',
        error_message='This value must contain only letters, numbers, hyphens and underscores.')
    first_name = forms.RegexField(
        label='First Name',
        max_length=30,
        regex=r'^[\w-]+$',
        error_message='This value must contain only letters, numbers, hyphens and underscores.')
    last_name = forms.RegexField(
        label='Last Name',
        max_length=30,
        regex=r'^[\w-]+$',
        error_message='This value must contain only letters, numbers, hyphens and underscores.')
    email = forms.RegexField(
        label='Email',
        max_length=30,
        regex=r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$',
        error_message='This value must contain only letters, numbers, hyphens and underscores.')

    class Meta:
        model = User
        fields=['first_name','last_name','username', 'email', 'password','confirm_password']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email Already Exists")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Username Take !!!")
        return username

    def clean_confirm_password(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('confirm_password')
        print p1,p2
        if p1!=p2:
            raise forms.ValidationError("Passwords must match")
        return p1
