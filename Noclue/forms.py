from django import forms

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    
    