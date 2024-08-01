# models.py
from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
        create_at =models.DateTimeField(auto_now=True)
        update_at = models.DateTimeField(auto_now=True)

        class Meta:
            abstract = True

class Catagory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name_plural = 'Catagories'


    def __str__(self):
        return self.title


class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    discription = models.TextField(null=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    raiting = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.PositiveSmallIntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Comment(BaseModel):
    user = models.ForeignKey(User,max_length=100, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    is_provide = models.BooleanField(default=False)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'


class Order(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order')
    quantity = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Order by {self.name.username} for {self.product.name}'


