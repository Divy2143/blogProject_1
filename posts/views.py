from django.shortcuts import render
from django.http import HttpResponse
from .models import Post    #you require the table name, whoose data you are gonna use below
# Create your views here.

def index(request) :
    #return HttpResponse("<h1>Welcome to my Django Project</h1>")
    posts = Post.objects.all() # this gets you all the objects created in "Post" table thus far
    return render(request, 'index.html', {'posts' : posts})

def post_pg(request, post_id) :
    post = Post.objects.get(id=post_id)
    return render(request, 'posts.html', {'post' : post})