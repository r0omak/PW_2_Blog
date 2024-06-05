from django.contrib import admin
from .models import Article, ArticleImage, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'main_page')
    list_filter = ['pub_date', 'main_page']
    search_fields = ['title', 'description']
    inlines = [ArticleImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
