
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('unico-apply-Tzura233i/universities/', views.Universities, name='Universities'),
    path('unico-apply-Tzura234i/about/', views.About_Us, name='About'),
    path('unico-apply-Tzura235i/contact-us', views.Contact_Us, name='Contact' ),
    path('unico-apply-Tzura236i-/register-account', views.register_view, name='Register'),
]

