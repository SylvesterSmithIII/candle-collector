from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Candle
from .forms import StoreForm


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
    store_form = StoreForm()
    return render(request, 'candles/detail.html', {
        'candle': candle, 'store_form': store_form
    })

def add_store(request, candle_id):
    # create a ModelForm instance using the data in request.POST
    form = StoreForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.candle_id = candle_id
        new_feeding.save()
    return redirect('detail', candle_id=candle_id)

class CandleCreate(CreateView):
    model = Candle
    fields = '__all__'

class CandleUpdate(UpdateView):
    model = Candle
    fields = ['scent', 'description', 'burn_time']

class CandleDelete(DeleteView):
    model = Candle
    success_url = '/candles'