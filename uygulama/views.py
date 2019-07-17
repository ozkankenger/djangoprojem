from django.shortcuts import render, get_object_or_404
from .models import Haberler, Kategori
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def anasayfa(request):
    post_list=Haberler.objects.all()
    query=request.GET.get('q')
    if query:
        post_list=post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 10) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_list = paginator.page(paginator.num_pages)

    categori=Kategori.objects.get(id=1)
    categori_list=categori.posts.all()
    paginator = Paginator(categori_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        categori_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        categori_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        categori_list = paginator.page(paginator.num_pages)

    context={'list':post_list,'categori_list':categori_list,}
    return render(request, 'index.html', context)

def gundem(request):
    post=Kategori.objects.get(id=1)
    liste=post.posts.all()
    context={
        'liste':liste,
    }
    return render(request, 'gundem.html', context)

def ekonomi(request):
    post=Kategori.objects.get(id=2)
    veri=post.posts.all()
    context={
        'veri':veri,
    }
    return render(request, 'ekonomi.html', context)

def siyaset(request):
    post=Kategori.objects.get(id=3)
    veri=post.posts.all()
    context={
        'veri':veri,
    }
    return render(request, 'siyaset.html', context)

def spor(request):
    post=Kategori.objects.get(id=4)
    veri=post.posts.all()
    context={
        'veri':veri,
    }
    return render(request, 'spor.html', context)

def detail(request, id):
    kayit=get_object_or_404(Haberler, id=id)
    context={
        'gelenveri':kayit,
    }
    return render(request, 'detail.html', context) 