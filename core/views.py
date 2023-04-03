from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


# Create your views here.
def index(request):
    """sss"""
    context = {"produtos": Produto.objects.all()}
    return render(request, "index.html", context)


def contato(request):
    "aaaa"

    form = ContatoForm(request.POST or None)

    if str(request.method) == "POST":

        if form.is_valid():
            form.send_email()
            messages.success(request, "Email enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar email")

    context = {"form": form}
    return render(request, "contato.html", context)


def produto(request):
    "ssss"
    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Produto guardado com sucesso")
                form = ProdutoModelForm()
            else:
                messages.error(request, "Erro ao guardar produto")
        else:
            form = ProdutoModelForm()
        context = {"form": form}
        return render(request, "produto.html", context)
    else:
        return redirect("index")
