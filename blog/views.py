from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    template_name = "index.html"
    context = {
        'posts': blogs
    }
    return render(request, template_name, context)

def posts(request):
    return HttpResponse("Posts Page")


def post_detail(request):
    return HttpResponse("Welcome to Post Detail Page")