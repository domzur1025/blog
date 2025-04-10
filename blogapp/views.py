from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm, CategoryForm
from .models import Post, Category

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by("-created_at")
    
    return render(request, 'blogapp/frontpage.html', {'posts': posts,})

def about(request):
    return render(request, 'blogapp/about.html')

def detail(request, category_slug, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, category__slug=category_slug, slug=slug)
    else:
        post = get_object_or_404(Post, slug=slug, category__slug=category_slug, status=Post.ACTIVE)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blogapp/detail.html', {'post': post, 'form':form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    
    return render(request, 'blogapp/category.html', {'category': category, 'posts': posts})

def categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = category.title.replace(" ", "-")
            category.save()
    
    form = CategoryForm()
    categories = list(Category.objects.all())
    
    return render(request, 'blogapp/categories.html', {'categories':categories, 'form':form})

def search(request):
    query = request.GET.get('query', '')
    
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    return render(request, 'blogapp/search.html', {'posts':posts, 'query':query})

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = post.title.replace(" ", "-")
            post.save()
            
            return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)
    else:
        form = PostForm()
        
    return render(request, 'blogapp/add.html', {'form': form,})

@login_required
def edit(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, category__slug=category_slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = post.title.replace(" ", "-")
            post.save()
            
            return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)
    else:
        
        form = PostForm(instance=post)
    return render(request, 'blogapp/add.html', {'form': form})

@login_required
def drafts(request):
    posts = list(Post.objects.filter(status=Post.DRAFT))
    return render(request, 'blogapp/drafts.html', {'posts': posts})