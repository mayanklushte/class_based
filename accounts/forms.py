from django import forms
from .models import *


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Mobile_Number', 'Address', 'City',
                  'State', 'Pin_Code', 'Profile_Picture')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Mobile_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'State': forms.TextInput(attrs={'class': 'form-control'}),
            'Pin_Code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ShopRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Shop_Name', 'Mobile_Number', 'Address',
                  'City', 'State', 'Pin_Code', 'Profile_Picture')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Mobile_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'State': forms.TextInput(attrs={'class': 'form-control'}),
            'Pin_Code': forms.TextInput(attrs={'class': 'form-control'}),
            'Shop_Name': forms.TextInput(attrs={'class': 'form-control'}),
        }

