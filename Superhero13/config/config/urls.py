"""config URL Configuration

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
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hero.views import PhotoDetailView, PhotoListView, HeroCreateView, HeroDeleteView, HeroUpdateView, AuthorAddView, CarouselView, NotesView


urlpatterns = [

    #database
    path('admin/', admin.site.urls),
    
    # Photos
    path('', PhotoListView.as_view(), name='hero_list'),
    path('<int:id>', PhotoDetailView.as_view(), name='detail_view'),
    path('add', HeroCreateView.as_view(),  name='add'),
    path('<int:pk>/edit', HeroUpdateView.as_view(),  name='edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='delete'),
    path('carousel', CarouselView.as_view(), name='carousel'),

    #user stuff
    path('accounts/', include('django.contrib.auth.urls')),
    path('author/add/', AuthorAddView.as_view(), name='author_add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
