from django import forms
from store.models import Profile , Review

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Metaa:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Firstname', 'Lastname', 'email', 'DOB', 'address', 'city', 'country', 'zipcode', 'tel']

