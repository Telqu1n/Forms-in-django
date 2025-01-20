from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, label='User')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Password')  
    email = forms.EmailField(max_length=100, label='Email',)
    
    