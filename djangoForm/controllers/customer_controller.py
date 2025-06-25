from django import forms
import re
from django.core.exceptions import ValidationError

class RegistroForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Requisitos de seguridad
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", password):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"\d", password):
            raise ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")
        return password