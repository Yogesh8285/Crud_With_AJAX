from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Signup),
    path('Dashboard',views.Dashboard),
    path('edit/',views.Edit,name='Edit'),
    path('Remove/', views.Remove, name='Remove'),
    path('Login/', views.Login),
    path('Logout/', views.Logout),
    path('save/', views.save,name='save'),
    path('add/', views.Signup,name='add'),
    path('testing/', views.testing,name='testing'),

]
