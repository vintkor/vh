from django.db import models
from vh.basemodel import BaseModel
from django.urls import reverse
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
#
#
# class Price(BaseModel):
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     def __str__(self):
#         return self.price


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_simple = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parameter = models.ManyToManyField('Parameter', through='ProductParameter', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:product-detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('manager:product-edit', args=[str(self.id)])


class Parameter(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ParameterValue(BaseModel):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.parameter, self.value)


class ProductParameter(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.ForeignKey(ParameterValue, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shop_product_parameter'

    def __str__(self):
        return '{} {} {}'.format(self.product, self.parameter, self.value)

    # def is_custom_value(self):
    #     if self.value in [value.value for value in self.parameter.parametervalue_set.all()]:
    #         return False
    #     return True
