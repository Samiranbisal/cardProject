from django.shortcuts import render, redirect
from .models import BlogPost 
# from .forms import BlogPostForm

def home(request):
    return render(request, 'home.html')
# Create your views here.
def about(request):
    return render(request, 'about.html')

def blog_create(request):
    return render(request, 'blog/blog_form.html', {'form': ''})

def blog_form(request):
    return render(request, 'blog_form.html')

def blog_list(request):
    return render(request, 'blog_list.html')

def blog_delete(request):
    return render(request, 'blog_delete.html')