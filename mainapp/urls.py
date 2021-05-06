from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('payment',views.payment,name='payment'),
    path('success',views.success,name='success'),
    path('contactus',views.contactus,name='contactus')
]
