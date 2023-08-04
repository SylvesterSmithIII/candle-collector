from django.shortcuts import render

candles = [
    {'name': 'Tranquil Lavender', 'scent': 'Lavender', 'description': 'Relaxing lavender-scented candle', 'burn_time': 20},
    {'name': 'Warm Vanilla', 'scent': 'Vanilla', 'description': 'Cozy vanilla-scented candle', 'burn_time': 15},
    {'name': 'Spiced Apple', 'scent': 'Apple and spices', 'description': 'Invigorating spiced apple-scented candle', 'burn_time': 18},
]

# Create your views here.
def home(request):
    # Include an .html file extention - unnline when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'candles/index.html', {
        'candles': candles
    })