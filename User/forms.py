from django.core.exceptions import ValidationError
from django.forms import forms
from User.models import UserProfile
from django.contrib.auth.models import User
from User.form_fields import *

__author__ = 'saeed'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    alias = forms.CharField(max_length=50, required=True)
    password = Password(max_length=50, widget=forms.PasswordInput(), required=True)
    confirm_password = Password(max_length=50, widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(max_length=70, required=True)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        pw1 = cleaned_data.get("password")
        pw2 = cleaned_data.get("confirm_password")
        if pw1 != pw2:
            raise ValidationError("Your confirmation of password doesn't match", code="password_confirmation_error");
        return cleaned_data


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }


class UserProfileRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['alias']


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


class ProfileUpdateForm(forms.Form):
    alias = forms.CharField(max_length=50, required=False)
    new_password = UpdatePassword(max_length=50, widget=forms.PasswordInput(), required=False)
    confirm_password = UpdatePassword(max_length=50, widget=forms.PasswordInput(), required=False)
    birthday = forms.CharField(required=False)

    def clean_birthday(self):
        date = self.cleaned_data['birthday']
        match_date = re.match('^(\d{2})/(\d{2})/(\d{4})$', date)
        if len(date) > 0:
            if not match_date:
                raise ValidationError('Date should be in DD/MM/YYYY format.', code='invalid_date')
            else:
                s = date.split("/")
                return s[2]+'-'+s[1]+'-'+s[0]
        else:
            return ''

    def clean(self):
        cleaned_data = super(ProfileUpdateForm, self).clean()

        print("validated")

        pw1 = cleaned_data.get("password")
        pw2 = cleaned_data.get("confirm_password")
        if pw1 != pw2:
            raise ValidationError("Your confirmation of password doesn't match", code="password_confirmation_error");

        return cleaned_data