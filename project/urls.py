"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from mundialistas.views import (index, PostListar, PostCrear, PostBorrar, 
                                PostActualizar, PostDetalle, UserSignUp,
                                UserLogin, UserLogout, AvatarActualizar,
                                UserActualizar, MensajeCrear, MensajeListar, 
                                MensajeDetalle, MensajeBorrar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mundialistas/', index, name="mundialistas-index"),
    path('mundialistas/listar/', PostListar.as_view(), name="mundialistas-listar"),
    path('mundialistas/crear/', staff_member_required(PostCrear.as_view()), name="mundialistas-crear"),
    path('mundialistas/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="mundialistas-borrar"),
    path('mundialistas/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="mundialistas-actualizar"),
    path('mundialistas/<int:pk>/detalle/', PostDetalle.as_view(), name="mundialistas-detalle"),
    path('mundialistas/signup/', UserSignUp.as_view(), name="mundialistas-signup"),
    path('mundialistas/login/', UserLogin.as_view(), name="mundialistas-login"),
    path('mundialistas/logout/', UserLogout.as_view(), name="mundialistas-logout"),
    path('mundialistas/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="mundialistas-avatars-actualizar"),
    path('mundialistas/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="mundialistas-users-actualizar"),
    path('mundialistas/mensajes/crear/', MensajeCrear.as_view(), name="mundialistas-mensajes-crear"),
    path('mundialistas/mensajes/listar/', MensajeListar.as_view(), name="mundialistas-mensajes-listar"),
    path('mundialistas/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mundialistas-mensajes-detalle"),
    path('mundialistas/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="mundialistas-mensajes-borrar"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)