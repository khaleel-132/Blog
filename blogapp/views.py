from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Post
from django.views.generic import ListView

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blogapp/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request,'blogapp/about.html',{'title':'About'})

