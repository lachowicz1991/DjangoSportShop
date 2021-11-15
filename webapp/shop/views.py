from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'shop/main.html')

def products(request):
	return render(request, 'shop/products.html')