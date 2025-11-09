from django import forms
from django.core.exceptions import ValidationError

class UsuarioRegistroForm(forms.Form):
    nombre = forms.CharField(
        max_length=255, 
        label="Nombre Completo",
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': 'Ej: Juan Pérez'
        })
    )
    documento = forms.CharField(
        max_length=50, 
        label="Documento",
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': 'Ej: 123456789'
        })
    )
    correo = forms.EmailField(
        max_length=255,
        label="Correo",
        widget=forms.EmailInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': 'usuario@email.com'
        })
    )
    telefono = forms.CharField(
        max_length=50,
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': '300 123 4567'
        })
    )
    clave = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': '••••••••'
        })
    )
    clave2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-[#231f36] border border-[#413768] rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-purple-400 placeholder-gray-500 text-base',
            'placeholder': '••••••••'
        })
    )

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("clave") != cleaned.get("clave2"):
            raise ValidationError("Las contraseñas no coinciden")
        return cleaned