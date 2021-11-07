from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('login/',views.login,name='login'),
    path('ragister/',views.ragister,name='ragister')

]


