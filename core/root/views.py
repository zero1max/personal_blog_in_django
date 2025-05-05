from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#
from .models import Article
from .forms import ArticleForm

def home(request):
    articles = Article.objects.order_by('-publishing_date')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return redirect('home')
    articles = Article.objects.all()
    return render(request, 'blog/admin_home.html', {'articles': articles})

@login_required
def new_article(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Maqola yaratildi, admin sahifasiga yo‘naltiramiz
    else:
        form = ArticleForm()

    return render(request, 'blog/new_article.html', {'form': form})


@login_required
def edit_article(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Maqola yangilandi
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})


@login_required
def delete_article(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        article.delete()
        return redirect('admin_home')  # Maqola o‘chirildi

    return render(request, 'blog/delete_article.html', {'article': article})

