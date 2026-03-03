
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

# Временный источник данных - список словарей


def index(request):
    """Главная страница — 5 последних опубликованных постов"""
    posts = Post.objects.select_related('category', 'location').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Страница отдельной публикации"""
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True  # Если категория скрыта — 404
    )

    posts = Post.objects.select_related('category', 'location').filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)
