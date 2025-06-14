from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact', views.contact, name = 'contact'),
    path('cleaning', views.cleaning, name = 'cleaning'),
    path('recruitment', views.recruitment, name = 'recruitment'),
    path('training', views.training, name = 'training'),
    path('contact-us', views.contact_us, name = 'contact-us'),
    path('enterpreneurship', views.enterpreneurship, name = 'enterpreneurship'),
    path('consultancy', views.consultancy ,name = 'consultancy'),
    path('estate-mananagement', views.estate_management, name = 'estate-management'),
]