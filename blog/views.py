
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

# Временный источник данных - список словарей

# ORM-запросы к базе данных:


def index(request):
    """Главная страница — 5 последних опубликованных постов"""
    # select_related — оптимизация, подгружает связанные объекты одним запросом
    posts = Post.objects.select_related('category', 'location').filter(
        # Дата публикации ≤ текущего времени
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    # Контекст — словарь данных, которые будут доступны в шаблоне
    # Ключ 'post_list' должен совпадать с {% for post in post_list %} в шаблоне
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
    # Контекст с одним постом
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница категории"""
    category = get_object_or_404(
        Category,
        # Ищем по slug (уникальный идентификатор)
        slug=category_slug,
        is_published=True  # Если категория скрыта — 404
    )

    posts = Post.objects.select_related('category', 'location').filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')
    # Контекст содержит категорию и список постов
    # В шаблоне: {{ category.title }}, {% for post in post_list %}
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)
