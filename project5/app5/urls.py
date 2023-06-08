from django.urls import path
from . import views
app_name='app5'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('gallary/',views.gallary,name='gallary'),
]