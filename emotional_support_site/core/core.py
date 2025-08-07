from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('crisis-help/', views.crisis_help, name='crisis_help'),
    path('assessment/', views.self_assessment, name='self_assessment'),
]