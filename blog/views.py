from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm


def create_article_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create_article.html', context)


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'blog/article_list.html', context)


def article_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }
    return render(request, 'blog/article_detail.html', context)