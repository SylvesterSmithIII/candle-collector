from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Candle, Wax
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

    id_list = candle.waxs.all().values_list('id')

    waxs_available = Wax.objects.exclude(id__in=id_list)

    return render(request, 'candles/detail.html', {
        'candle': candle, 'store_form': store_form, 'waxs': waxs_available
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

def assoc_wax(request, candle_id, wax_id):
    
    Candle.objects.get(id=candle_id).waxs.add(wax_id)
    return redirect('detail', candle_id=candle_id)


def remove_wax(request, candle_id, wax_id):
    
    Candle.objects.get(id=candle_id).waxs.remove(wax_id)
    return redirect('detail', candle_id=candle_id)


class CandleCreate(CreateView):
    model = Candle
    fields = ['name', 'scent', 'description', 'burn_time']

class CandleUpdate(UpdateView):
    model = Candle
    fields = ['scent', 'description', 'burn_time']

class CandleDelete(DeleteView):
    model = Candle
    success_url = '/candles'

# wax classes

class WaxList(ListView):
    model = Wax

class WaxCreate(CreateView):
    model = Wax
    fields = '__all__'

class WaxDetail(DetailView):
    model = Wax

class WaxUpdate(UpdateView):
    model = Wax
    fields = '__all__'

class WaxDelete(DeleteView):
    model = Wax
    success_url = '/waxs'
