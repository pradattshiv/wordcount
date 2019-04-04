from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name ='home'),
    # path('page1/', views.page1),
    path('countss/',views.count, name ='count1')
]
