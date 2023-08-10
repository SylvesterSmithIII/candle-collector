from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Candle, Wax
from .forms import StoreForm


# Create your views here.
def home(request):
    # Include an .html file extention - unnline when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def candles_index(request):
    candles = Candle.objects.filter(user=request.user)
    return render(request, 'candles/index.html', {
        'candles': candles
    })

@login_required
def candle_detial(request, candle_id):
    candle = Candle.objects.get(id=candle_id)
    store_form = StoreForm()

    id_list = candle.waxs.all().values_list('id')

    waxs_available = Wax.objects.exclude(id__in=id_list)

    return render(request, 'candles/detail.html', {
        'candle': candle, 'store_form': store_form, 'waxs': waxs_available
    })

@login_required
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

@login_required
def assoc_wax(request, candle_id, wax_id):
    
    Candle.objects.get(id=candle_id).waxs.add(wax_id)
    return redirect('detail', candle_id=candle_id)

@login_required
def remove_wax(request, candle_id, wax_id):
    
    Candle.objects.get(id=candle_id).waxs.remove(wax_id)
    return redirect('detail', candle_id=candle_id)


class CandleCreate(LoginRequiredMixin, CreateView):
    model = Candle
    fields = ['name', 'scent', 'description', 'burn_time']

class CandleUpdate(LoginRequiredMixin, UpdateView):
    model = Candle
    fields = ['scent', 'description', 'burn_time']

class CandleDelete(LoginRequiredMixin, DeleteView):
    model = Candle
    success_url = '/candles'

# wax classes

class WaxList(LoginRequiredMixin, ListView):
    model = Wax

class WaxCreate(LoginRequiredMixin, CreateView):
    model = Wax
    fields = '__all__'

class WaxDetail(LoginRequiredMixin, DetailView):
    model = Wax

class WaxUpdate(LoginRequiredMixin, UpdateView):
    model = Wax
    fields = '__all__'

class WaxDelete(LoginRequiredMixin, DeleteView):
    model = Wax
    success_url = '/waxs'

@login_required
def signup(request):
    error_message = ''
    # this will be ran if user tries to signup
    if request.method == 'POST':
      
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save user info
            user = form.save()
            # log user in
            login(request, user)
            # redirect user
            return redirect('index')
      
        else:
            error_message = 'Invalid sign up - try again'
    
    # this will happen when GET method/ browsing to this URL
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
      