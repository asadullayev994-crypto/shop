from django.db import models
from django.conf import settings
from shared.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(BaseModel):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.title


class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    text = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class Saved(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('product', 'user')