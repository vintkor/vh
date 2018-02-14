from django.contrib import admin
from .models import Page, Text, Image
from django.contrib.contenttypes.admin import GenericStackedInline


class TextInline(GenericStackedInline):
    extra = 0
    model = Text
    prepopulated_fields = {'slug': ('title',)}


class ImageInline(GenericStackedInline):
    extra = 0
    model = Image
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (TextInline, ImageInline)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
