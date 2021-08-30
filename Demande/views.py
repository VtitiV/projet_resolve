from django.shortcuts import render


def demandedepart(request):
    return render(request, "demandetemplates/demande.html")

def demande_de_compte(request):
    return render(request, "demandetemplates/comptes/choixtypedecomptes.html")


