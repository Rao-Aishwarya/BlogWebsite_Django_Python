from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from blog import models
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
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
            return redirect('/login')

    return render(request, 'blog/login.html')




#New feature search functionality
@login_required
def home(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(author__username__icontains=query)

        if not posts:
            message = f"No posts found by author '{query}'"
        else:
            message = None
    else:
        posts = Post.objects.all()
        
    context = {
        'posts': posts,
        'query': query,
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


#New feature delete post
@login_required
def myPost(request):
    try:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            if post_id:
                try:
                    post = get_object_or_404(Post, id=post_id)
                    post.delete()
                except Exception as e:
                    # Handle exceptions if needed
                    print(f"Error deleting post: {e}")
                return redirect('/mypost')
            else:
                # Handle the case where post_id is not provided
                return redirect('/mypost')  # or show an error message

        context = {
            'posts': Post.objects.filter(author=request.user)
        }

        return render(request, 'blog/mypost.html', context)
    
    except Exception as e:
        return redirect('/loginn')



def signout(request):
    logout(request)
    return redirect('/loginn')

