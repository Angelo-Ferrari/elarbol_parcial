from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
                  path('', views.inicio, name='inicio'),
                  path('inicio/', views.inicio, name='inicio'),
                  path('tienda/', views.tienda, name='tienda'),
                  path('registro/', views.registro, name='registro'),
                  path('login/', LoginView.as_view(template_name='elarbol/login.html'), name='login'),
                  path('logout/', LogoutView.as_view(template_name='elarbol/logout.html'), name='logout'),
                  path('agregar/', views.agregar, name='agregar'),
                  path('editar/<int:id>', views.editar, name='editar'),
                  path('eliminar/<id>/', views.eliminar, name='eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

