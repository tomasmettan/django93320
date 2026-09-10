from django.shortcuts import render, get_object_or_404, redirect
from home.models import Pintura
from home.forms import PinturaForm, MiFormularioDeCreacion #
from django.views.generic.edit import UpdateView, DeleteView #
from django.urls import reverse_lazy #
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #
from django.contrib.auth import login #


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def listado_de_pinturas(request):

    nombre = request.GET.get("nombre")
    pinturas = Pintura.objects.all()

    if nombre:
        pinturas = pinturas.filter(nombre__icontains=nombre)

    return render(request, 'home/listado_de_pinturas.html', {'pinturas': pinturas})


def ver_pintura(request, pk):
    pintura = get_object_or_404(Pintura, pk=pk)
    context = {
        "pintura": pintura
    }

    return render(request, "home/ver_pintura.html", context)


def crear_pintura(request):
    if request.method == "POST":
        form = PinturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_pinturas")
    else:
        form = PinturaForm()

    return render(request, "home/crear_pintura.html", {"form": form})


# Clases
##########
class EditarPintura(UpdateView):
    model = Pintura
    form_class = PinturaForm
    template_name = "home/editar_pintura.html"
    success_url = reverse_lazy('listar_pinturas')


class EliminarPintura(DeleteView):
    model = Pintura
    template_name = "home/eliminar_pintura.html"
    success_url = reverse_lazy('listar_pinturas')


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()

            login(request, usuario)

            return redirect("home")
    else:
        form = AuthenticationForm()

        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingresá tu usuario'
        })

        form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingresá tu contraseña'
        })

    return render(request, 'home/iniciar_sesion.html', {"form": form})


def registro(request):

    if request.method == 'POST':
        form = MiFormularioDeCreacion(request.POST)  # Permite crear un formulario de autenticación de usuario y lo valida.
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos.

            return redirect("home")
    else:
        form = MiFormularioDeCreacion()

    return render(request, 'home/registro.html', {"form": form})

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------