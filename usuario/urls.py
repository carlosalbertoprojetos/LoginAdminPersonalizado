
from django.urls import path
from Base_Django import settings
from django.conf.urls.static import static

from . import views

app_name = 'usuario'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # path('cadastro/', views.register_View, name='register'),
    path('cadastrar/', views.RegisterView.as_view(), name='register'),
    path('perfil/', views.ProfileView.as_view(), name='profile'),
]


# faz com que o DEBUG seja False caso colocado em produção
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
