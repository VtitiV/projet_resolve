from django.shortcuts import render


def user_views(request):
    return render(request, "usertemplate/user.html")

