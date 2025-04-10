from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Post 

# Create your views here.
def robots_txt(request):
    text = [
        'User-Agent: *',
        'Disallow: /admin/',
    ]
    
    return HttpResponse("\n".join(text), content_type='text/plain')

def error_view(request, exception=None, status_code=500, title="Błąd", message="Coś poszło nie tak..."):
    return render(request, "core/error.html", {
        "status_code": status_code,
        "title": title,
        "message": message,
    }, status=status_code)

def handler404(request, exception):
    return error_view(request, exception, status_code=404, title="Nie znaleziono", message="Strona nie istnieje.")

def handler500(request):
    return error_view(request, status_code=500, title="Błąd serwera", message="Wewnętrzny błąd serwera.")

def handler403(request, exception):
    return error_view(request, exception, status_code=403, title="Brak dostępu", message="Nie masz uprawnień do tej strony.")

def handler400(request, exception):
    return error_view(request, exception, status_code=400, title="Złe żądanie", message="Nieprawidłowe żądanie.")