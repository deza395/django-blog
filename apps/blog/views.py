from django.shortcuts import render

from .models import Post , Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(status = True)
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})


def tips(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        status= True,
        category=Category.objects.get(name__iexact='tips')
     )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tips.html',{'posts':posts})


def python(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        status= True,
        category=Category.objects.get(name__iexact='python')
     )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'python.html',{'posts':posts})

    

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        status= True,
        category=Category.objects.get(name='tecnologia')
     )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html',{'posts':posts})

def ambiente(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        status= True,
        category=Category.objects.get(name='ambiente')
     )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'ambiente.html',{'posts':posts})


def detailsPost(request,slug):
    post  = get_object_or_404(Post,slug = slug)
    print(post)
    return render(request, 'post.html',{'detailsPost':post})


