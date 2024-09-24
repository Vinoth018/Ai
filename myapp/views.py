from django.shortcuts import render

# Create your views here.
def language_translation(request):
    return render(request, 'myapp/language.html')

def products(request):
    return render(request, 'myapp/products.html')


def subtitles(request):
    return render(request, 'myapp/subtitles.html')