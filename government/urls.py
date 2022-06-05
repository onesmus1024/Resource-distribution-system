from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('import/', views.Import.as_view(), name='import'),
    path('localsupplier/', views.LocalSupplierView.as_view(), name='localsupplier'),
    path('consumer/', views.ConsumerView.as_view(), name='consumer'),
    path('info/', views.info, name='info'),
    
]