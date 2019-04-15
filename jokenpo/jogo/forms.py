from django import forms


class UserForm(forms.Form):
    user = forms.CharField(label='Usuario', max_length=20)
    password = forms.CharField(label='Senha', max_length=20,
                               widget=forms.PasswordInput)
