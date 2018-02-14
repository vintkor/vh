from django.db import models
from vh.basemodel import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


class Page(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-detail', args=[str(self.id)])

    def get_fields(self):
        list_fields = [
            Image.objects.filter(object_id=self.id),
            Text.objects.filter(object_id=self.id),
        ]

        new_some = {}
        for qs in list_fields:
            for i in qs:
                f_type = (i._meta.label).split('.')[1]
                new_some['{}__{}'.format(f_type.lower(), i.slug)] = i.content

        return new_some


class Image(BaseModel):
    title = models.CharField(max_length=55)
    slug = models.SlugField()
    content = models.ImageField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.content_object)


class Text(BaseModel):
    title = models.CharField(max_length=55)
    slug = models.SlugField()
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.content_object)
