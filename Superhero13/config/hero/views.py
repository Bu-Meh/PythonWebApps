from django.shortcuts import render

# Create your views here.
from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from .models import Hero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HeroListView(TemplateView):
    template_name = 'heroes.html'
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class HeroView(TemplateView):
    template_name = 'notes.html'
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class CarouselView(TemplateView):
    template_name = 'Carousel.html'
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        return dict(hero=Hero.objects.get(pk=i))


class HeroCreateView(LoginRequiredMixin, CreateView):  
    template_name = "add.html"
    model = Hero
    fields = '__all__'

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'delete.html'
    success_url = reverse_lazy('hero_list')

class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'
