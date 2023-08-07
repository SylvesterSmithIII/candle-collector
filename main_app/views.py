from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Candle


# Create your views here.
def home(request):
    # Include an .html file extention - unnline when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def candles_index(request):
    candles = Candle.objects.all()
    return render(request, 'candles/index.html', {
        'candles': candles
    })

def candle_detial(request, candle_id):
    candle = Candle.objects.get(id=candle_id)
    return render(request, 'candles/detail.html', {
        'candle': candle
    })

class CandleCreate(CreateView):
    model = Candle
    fields = '__all__'

class CandleUpdate(UpdateView):
    model = Candle
    fields = ['scent', 'description', 'burn_time']

class CandleDelete(DeleteView):
    model = Candle
    success_url = '/candles'