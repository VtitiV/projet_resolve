from django.shortcuts import render


def incidentdepart(request):
    return render(request, "incidentstemplates/incidents.html")

