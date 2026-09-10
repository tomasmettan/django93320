from django import forms
from home.models import Pintura
from django.contrib.auth.forms import UserCreationForm #
from django.contrib.auth.models import User #


class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ("nombre", "autor", "descripcion")


class MiFormularioDeCreacion(UserCreationForm): #
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None
        }

    def save(self, commit=True):
        user = super(MiFormularioDeCreacion, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user