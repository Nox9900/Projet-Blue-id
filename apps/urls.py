from django.urls import path
from .import views
app_name = 'apps'

urlpatterns = [
    path('' , views.index , name='index'),
    path('main/', views.main , name='main'),
    path('personal/', views.list_personal_office , name='personal'),
    path('user/', views.list_users , name='user'),
]
