from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products:filtered_products', args=[self.slug])



    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    url_flipkart = models.CharField(max_length=250, db_index=True)
    url_jiomart = models.CharField(max_length=250, db_index=True)
    url_amazon = models.CharField(max_length=250, db_index=True)

    price_flipkart = models.IntegerField(default=0)
    price_jiomart = models.IntegerField(default=0)
    price_amazon = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)
    # make all thumbnails at most 140x140pixels

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
