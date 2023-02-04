from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, TabularInlineJalaliMixin


from .models import Product, Comment


class CommentInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'stars','active',)
    ordering = ('author', 'active')
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_modified', 'active')
    ordering = ('title', 'price', '-datetime_modified', 'active')

    inlines = (CommentInline, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'stars', 'active')
    ordering = ('product', 'author', 'active', 'body')
