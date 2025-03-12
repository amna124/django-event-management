from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
    #adding comments in the file to make some changes and check if changes are pushed or not
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password'
    }))
