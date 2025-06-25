from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request, "home.html")
	

def vista_bienvenida(request):
    return render(request, 'djangoForm/inside.html')