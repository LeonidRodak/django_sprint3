from django.shortcuts import render


# Create your views here.
def about(request):
    """Страница «О проекте»"""
    return render(request, 'about.html')


def rules(request):
    """Страница «Правила проекта»"""
    return render(request, 'rules.html')
