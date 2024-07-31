from pyexpat.errors import messages
import re
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from blog import models
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def sanitize_query(query):
    # Define a regular expression pattern for allowed characters (alphanumeric and spaces)
    allowed_characters = re.compile(r'^[\w\s]*$')
    return allowed_characters.match(query)

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')

        if User.objects.filter(username=name).exists():
            return render(request, 'blog/signup.html', {
                'error_message': 'Username already exists'
            })
        
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'blog/signup.html')



def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return render(request, 'blog/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'blog/login.html')


#New feature search functionality
@login_required
def home(request):
    query = request.GET.get('q', '')
    
    if query:
        if not sanitize_query(query):
            # Invalid query: contains special characters
            message = "Invalid characters in search query."
            posts = []
        else:
            # Valid query
            posts = Post.objects.filter(author__username__icontains=query)

            if not posts:
                message = f"No posts found by author '{query}'"
            else:
                message = None
    else:
        posts = Post.objects.all()
        message = None
        
    context = {
        'posts': posts,
        'query': query,
        'message': message,
    }
    return render(request, 'blog/home.html', context)


@login_required
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'blog/newpost.html')


@login_required
def myPost(request):
    if request.method == 'POST':
        
        action = request.POST.get('action')
        post_id = request.POST.get('post_id')

        if action == 'delete' and post_id:
            delete_post(post_id)
        elif action == 'update' and post_id:
            title = request.POST.get('title')
            content = request.POST.get('content')
            return redirect('update-post/{{post_id}}', post_id=post_id)

        return redirect('/mypost')

    # GET request
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/mypost.html', context)


@login_required
def updatePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            post.title = title
            post.content = content
            post.save()
            return redirect('/mypost')

    context = {
        'post': post
    }
    return render(request, 'blog/updatePost.html', context)


def delete_post(post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    except Exception as e:
        # Handle exceptions
        print(f"Error deleting post: {e}")



def signout(request):
    logout(request)
    return redirect('/loginn')

