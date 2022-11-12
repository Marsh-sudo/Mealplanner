from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','email')

        USERNAME_FIELD = 'username'

    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class LoginUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']