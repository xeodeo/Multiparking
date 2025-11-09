import hashlib
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from roles.models import Rol
from .forms import UsuarioRegistroForm


def registro_usuario(request):
    registrado = False
    error_registro = None
    mostrar_modal_registro = False

    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        clave = form.data.get("clave")
        clave2 = form.data.get("confirmar_clave")

        if clave2 is not None and clave != clave2:
            error_registro = "Las contraseñas no coinciden."
            mostrar_modal_registro = True

        elif form.is_valid():
            nombre = form.cleaned_data["nombre"]
            documento = form.cleaned_data["documento"]
            correo = form.cleaned_data["correo"]
            telefono = form.cleaned_data["telefono"]
            clave_hash = hashlib.sha256(clave.encode()).hexdigest()

            try:
                rol_usuario = Rol.objects.get(id=2)
            except Rol.DoesNotExist:
                error_registro = "Rol 'USUARIO' no existe. Crea el rol en el administrador."
                mostrar_modal_registro = True
            else:
                if Usuario.objects.filter(usuDocumento=documento).exists():
                    error_registro = "Ya existe un usuario con ese documento."
                    mostrar_modal_registro = True
                elif Usuario.objects.filter(usuCorreo=correo).exists():
                    error_registro = "Ya existe un usuario con ese correo."
                    mostrar_modal_registro = True
                else:
                    Usuario.objects.create(
                        usuDocumento=documento,
                        usuNombreCompleto=nombre,
                        usuCorreo=correo,
                        usuTelefono=telefono,
                        usuClaveHash=clave_hash,
                        usuEstado="ACTIVO",
                        fkIdRol=rol_usuario
                    )
                    # Redirige con flag de éxito para mostrar el popup
                    return redirect('/?registro_exitoso=1')
        else:
            mostrar_modal_registro = True

    else:
        form = UsuarioRegistroForm()

    # Si venimos del registro exitoso:
    if request.GET.get('registro_exitoso') == '1':
        registrado = True
        form = UsuarioRegistroForm()  # limpiar formulario

    return render(request, "web/home.html", {
        "form_registro": form,
        "registro_exitoso": registrado,
        "error_registro": error_registro,
        "mostrar_modal_registro": mostrar_modal_registro,
    })


def login_view(request):
    return render(request, "web/login.html")
