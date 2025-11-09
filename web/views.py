import hashlib
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from roles.models import Rol
from .forms import UsuarioRegistroForm


# -----------------------------
# HOME / REGISTRO DE USUARIOS
# -----------------------------
def home(request):
    registrado = False
    error_registro = None
    mostrar_modal_registro = False
    login_error = None
    mostrar_modal_login = False

    # --- PROCESO DE REGISTRO ---
    if request.method == "POST" and not request.POST.get("action") == "login":
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
                rol_usuario = Rol.objects.get(id=2)  # usuario normal
            except Rol.DoesNotExist:
                error_registro = "Rol 'USUARIO' no existe. Crea el rol en el administrador."
                mostrar_modal_registro = True
            else:
                # Validaciones de duplicado
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
                    # 🔁 Redirigir para mostrar popup éxito
                    return redirect('/?registro_exitoso=1')

        else:
            # Si no pasó la validación del form (campos vacíos o tipo)
            error_registro = "Por favor revisa los campos e intenta nuevamente."
            mostrar_modal_registro = True
    else:
        form = UsuarioRegistroForm()

    # --- Si se completó el registro exitoso ---
    if request.GET.get('registro_exitoso') == '1':
        registrado = True
        form = UsuarioRegistroForm()

    # --- Si hubo error de login (por redirect) ---
    if request.GET.get('login_error'):
        login_error = request.GET.get('login_error')
        mostrar_modal_login = True

    return render(request, "web/home.html", {
        "form_registro": form,
        "registro_exitoso": registrado,
        "error_registro": error_registro,
        "mostrar_modal_registro": mostrar_modal_registro,
        "login_error": login_error,
        "mostrar_modal_login": mostrar_modal_login,
    })


# -----------------------------
# LOGIN DE USUARIOS
# -----------------------------
def login_view(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")

        if not correo or not clave:
            return redirect('/?login_error=Debes ingresar ambos campos.')

        clave_hash = hashlib.sha256(clave.encode()).hexdigest()

        try:
            usuario = Usuario.objects.select_related('fkIdRol').get(
                usuCorreo=correo,
                usuClaveHash=clave_hash,
                usuEstado="ACTIVO"
            )
        except Usuario.DoesNotExist:
            return redirect('/?login_error=Correo o contraseña incorrectos.')

        # Guardar sesión
        request.session['usuario_id'] = usuario.id
        request.session['usuario_nombre'] = usuario.usuNombreCompleto
        request.session['usuario_rol'] = usuario.fkIdRol.id

        # Redirección por rol
        if usuario.fkIdRol.id == 1:
            return redirect('/panel-vigilante/')
        elif usuario.fkIdRol.id == 2:
            return redirect('/panel-usuario/')
        else:
            return redirect('/')

    return redirect('/')


# -----------------------------
# LOGOUT
# -----------------------------
def logout_view(request):
    request.session.flush()
    return redirect('/')


# -----------------------------
# PANELES POR ROL
# -----------------------------
def panel_vigilante(request):
    if request.session.get('usuario_rol') != 1:
        return redirect('/')
    return render(request, "web/panel_vigilante.html", {
        "usuario": request.session.get('usuario_nombre'),
    })


def panel_usuario(request):
    if request.session.get('usuario_rol') != 2:
        return redirect('/')
    return render(request, "web/panel_usuario.html", {
        "usuario": request.session.get('usuario_nombre'),
    })
