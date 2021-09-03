from django.http.response import HttpResponse, HttpResponseBase, HttpResponseRedirect
from django.shortcuts import render
from django import forms


class UploadInfoActivosForm(forms.Form):
    title = forms.CharField(max_length=50)
    excel = forms.FileField()


# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadInfoActivosForm(request.POST, request.FILES)

        if form.is_valid():
            # Process excel --> save data to model --> show filters and rest of elements

            return HttpResponseRedirect("display", request)
        else:
            return render(request, "eff/upload.html", context={ 
                "form": form
            })

    return render(request, "eff/upload.html", context={
        "form": UploadInfoActivosForm()
    })


def display(request):
    return render(request, "eff/display.html")