from django.urls import path
from .views import home,districts, taluks, hoblis, save_form_data, get_form_data

urlpatterns = [

    path('', home, name='home'),
    path('districts/', districts, name='districts'),
    path('taluks/<int:district_id>/', taluks, name='taluks'),
    path('hoblis/<int:taluk_id>/', hoblis, name='hoblis'),
    path('save/', save_form_data, name='save_form_data'),

    # GET by ID
    path('save/<int:id>/', get_form_data)
]