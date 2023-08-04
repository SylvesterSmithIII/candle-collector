from django.shortcuts import render

candles = [
    {'name': 'Tranquil Lavender', 'scent': 'Lavender', 'description': 'Relaxing lavender-scented candle', 'burn_time': 20},
    {'name': 'Warm Vanilla', 'scent': 'Vanilla', 'description': 'Cozy vanilla-scented candle', 'burn_time': 15},
    {'name': 'Spiced Apple', 'scent': 'Apple and spices', 'description': 'Invigorating spiced apple-scented candle', 'burn_time': 18},
    {'name': 'Fresh Linen', 'scent': 'Clean and crisp', 'description': 'Fresh linen-scented candle for a clean ambiance', 'burn_time': 12},
    {'name': 'Forest Pine', 'scent': 'Pine and earth', 'description': 'Bring the outdoors in with this forest pine-scented candle', 'burn_time': 22},
    {'name': 'Citrus Burst', 'scent': 'Citrus fruits', 'description': 'Energizing citrus burst-scented candle for a lively atmosphere', 'burn_time': 17},
]


# Create your views here.
def home(request):
    # Include an .html file extention - unnline when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def candles_index(request):
    return render(request, 'candles/index.html', {
        'candles': candles
    })