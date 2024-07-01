from django.urls import path,include
from main import views

urlpatterns = [
    path('Auto/',views.Auto.as_view(),name="auto"),
    path('',views.home,name='base_url'),
    path('next/',views.next_message),
    path('prev/',views.prev_message),
    path('Auto_page',views.Auto_page),
    path('buffer',views.buffer),
]