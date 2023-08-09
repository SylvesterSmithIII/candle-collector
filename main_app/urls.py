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
    path('candles/<int:candle_id>/add_store/', views.add_store, name='add_store'),
    path('waxs/', views.WaxList.as_view(), name="waxs_index"),
    path('waxs/create/', views.WaxCreate.as_view(), name="waxs_create"),
    path('waxs/<int:pk>/', views.WaxDetail.as_view(), name="wax_detail"),
    path('waxs/<int:pk>/update/', views.WaxUpdate.as_view(), name="waxs_update"),
    path('waxs/<int:pk>/delete/', views.WaxDelete.as_view(), name="waxs_delete"),
    path('candles/<int:candle_id>/assoc_wax/<int:wax_id>/', views.assoc_wax, name='assoc_wax'),
    path('candles/<int:candle_id>/remove/<int:wax_id>/', views.remove_wax, name='remove_wax'),
]