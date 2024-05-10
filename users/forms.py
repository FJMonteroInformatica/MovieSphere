from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellidos")
    email = forms.EmailField(max_length=150, required=True, label="Correo electrónico")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmación de la contraseña", required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellidos")
    email = forms.EmailField(max_length=150, required=True, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Nueva contraseña", required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            if field.required:
                field.widget.attrs.update({'class': 'required'})