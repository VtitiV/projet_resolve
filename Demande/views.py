from django.shortcuts import render


def demandedepart(request):
    return render(request, "demandetemplates/demande.html")


