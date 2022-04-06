from django.shortcuts import render


def dashboard(request, id):
    return render(request, 'customAdmin/index.html')