from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from bookmarks.models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #validation
        if password != confirm_password:
            messages.error(request,"Passwords do not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email is already registered!")
            return redirect('signup')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user) #Auto login after signup
        messages.success(request,"Account created successfully!")
        return redirect('dashboard')
    
    return render(request,"signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect('login') # redirect to login after logout

@login_required(login_url="login")
def dashboard(request):
    if request.method == "POST":
        title = request.POST['title']
        url = request.POST['url']
        category = request.POST['category']
        if category == "":
            category = Bookmark._meta.get_field('category').get_default()
        Bookmark.objects.create(user = request.user,title=title,url=url,category=category)
        return redirect('dashboard')
    query = request.GET.get('q','')
    '''Agar q parameter mil gaya toh uski value query mein store karo.
    Agar nahi mila, toh '' (empty string) use karo.'''
    bookmarks = Bookmark.objects.filter(user=request.user)
    if query:
        bookmarks = bookmarks.filter(title__icontains=query)
        #icontains = ignore case + contains (partial match)
    return render(request,"dashboard.html",locals())

@login_required(login_url = 'login')
def edit_bookmark(request,bookmark_id):
    bookmark = get_object_or_404(Bookmark,id=bookmark_id,user=request.user)
    categories = CATEGORY_CHOICES
    if request.method == "POST":
        bookmark.title = request.POST['title']
        bookmark.url = request.POST['url']
        bookmark.category = request.POST['category']
        bookmark.save()
        return redirect('dashboard')
    return render(request,"edit_bookmark.html",locals())

@login_required(login_url = 'login')
def delete_bookmark(request,bookmark_id):
    bookmark = get_object_or_404(Bookmark,id=bookmark_id,user=request.user)
    bookmark.delete()
    return redirect('dashboard')





        
