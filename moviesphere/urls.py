"""
URL configuration for MovieSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from movies import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin

class MyPasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'
    success_message = "Your password was successfully updated!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='password'),
    path('signup/', views.signup, name='signup'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)