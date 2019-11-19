from django.urls import path

from CHMS import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('pred/', views.diagnosis, name='pred'),
    path('pred_res/<str:disease>', views.results, name='pred_res'),
    path('pred_symps/', views.symptoms_reciever, name='symptoms'),
]
