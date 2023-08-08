from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('candles/', views.candles_index, name='index'),
    path('candles/<int:candle_id>/', views.candle_detial, name='detail'),
    path('candles/create/', views.CandleCreate.as_view(), name="candles_create"),
    path('candles/<int:pk>/update/', views.CandleUpdate.as_view(), name="candles_update"),
    path('candles/<int:pk>/delete/', views.CandleDelete.as_view(), name="candles_delete"),
    path('candles/<int:candle_id>/add_store/', views.add_store, name='add_store')
]