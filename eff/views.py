from eff.models import InfoActivosModel
from eff import auxiliar

from django.http.response import HttpResponse, HttpResponseBase, HttpResponseRedirect
from django.shortcuts import render
from django import forms


class UploadInfoActivosForm(forms.Form):
    excel = forms.FileField()


# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadInfoActivosForm(request.POST, request.FILES)

        if form.is_valid():
            mercado = auxiliar.Mercado(request.FILES["excel"].read())

            ids = []
            for m in InfoActivosModel.objects.all():
                ids.append(m.id_mercado)

            if str(mercado) not in ids:
                InfoActivosModel(id_mercado=str(mercado), rentabilidades={}, volatilidades={}).save()
            else:
                entry = InfoActivosModel.objects.get(id_mercado=str(mercado))
                entry.rentabilidades = {}
                entry.volatilidades = {}
                entry.save()
            
            return HttpResponseRedirect("display", request)
        else:
            return render(request, "eff/upload.html", context={ 
                "form": form
            })

    return render(request, "eff/upload.html", context={
        "form": UploadInfoActivosForm()
    })


def display(request):
    mercados = []

    for e in InfoActivosModel.objects.all():
        mercados.append(e.id_mercado)

    return render(request, "eff/display.html", context={
        "mercados": mercados
    })