from django import forms
from django.core.validators import URLValidator
from .models import user

class users(forms.Form):
    Fname = forms.CharField(label='First Name', widget= forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"First Name"
        }
    ))
    Lname = forms.CharField(label='Last Name', widget= forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Last Name"
        }
    ))
    age = forms.IntegerField(widget= forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Age"
        }
    ))
    email = forms.EmailField(label='Email',widget= forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Email"
        }
    ))
    Password = forms.CharField(label= "Password",widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))
    Password2 = forms.CharField(label= "Confirm Password",widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        }
    ))


    def clean_Password2(self):
        pass1 = self.cleaned_data.get('Password')
        pass2 = self.cleaned_data.get('Password2')
        print pass1, pass2
        if pass1 !=pass2:
            raise forms.ValidationError("Passwords do not match")
        return pass1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = user.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email Already Exists")
        return email


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
