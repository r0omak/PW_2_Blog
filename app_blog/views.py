from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category
from django.shortcuts import get_object_or_404

class ArticleListView(ListView):
    model = Article
    template_name = 'app_blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug', None))
        return context
       
class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]
        return context

    def get_queryset(self):
        return Category.objects.all()

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = context['item'].images.all() if context['item'].images.all() else None
        return context

class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs.get('slug', None))
        return context

    def get_queryset(self):
        return Article.objects.all()

class ArticleCategoryList(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category__slug__in=[self.kwargs['slug']]).distinct()
