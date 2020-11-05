from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# superuser pass = gonelovepy
# Create your views here.
# def home(req):
#     return render(req, 'index.html')
# def postbro(req):
#     return render(req, 'postbro.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostView(DetailView):
    model = Post
    template_name = 'postDetail.html'


class PostbroView(CreateView):
    model = Post
    template_name = 'postbro.html'
    fields = '__all__'