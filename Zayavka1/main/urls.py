from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('type_obr/', TypeObrView.as_view(), name='type_obr'),
    path('client/', ClientView.as_view(), name='client'),
    path('type_work/', TypeWorkView.as_view(), name='type_work'),
    path('obr/', ObrView.as_view(), name='obr'),
    path('workbyobr_view/', WordByObrView.as_view(), name='workbyobr_view'),
    path('worker/', WorkerView.as_view(), name='worker'),
    path('workinobr/', ObrInWork.as_view(), name='workinobr'),
    path('workobr/', WorkObr.as_view(), name='workobr'),

    path('create_type_obr/', CreateTypeObrView.as_view(), name='create_type_obr'),
    path('create_client/', CreateClientView.as_view(), name='create_client'),
    path('create_type_work/', CreateTypeWorkView.as_view(), name='create_type_work'),
    path('create_obr/', CreateObrView.as_view(), name='create_obr'),
    path('create_workbyobr_view/', CreateWordByObrView.as_view(), name='create_workbyobr_view'),

    path('register/', RegistrationFormView.as_view(), name='register'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('logout/', MainLogoutView.as_view(), name='logout'),
]