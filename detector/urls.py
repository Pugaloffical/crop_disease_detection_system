from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('frontend/', views.frontend, name='frontend'),
    path('scanner/', views.scanner, name='scanner'),
    path('result/<int:upload_id>/', views.result, name='result'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search, name='search'),
    path('weather/', views.weather, name='weather'),
    path('encyclopedia/', views.encyclopedia, name='encyclopedia'),
    path('reports/', views.reports, name='reports'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('diseases/', views.disease_catalog, name='disease_catalog'),
    path('diseases/<slug:slug>/', views.disease_detail, name='disease_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='detector/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
]
