from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Product(models.Model):
    MOBILE = 'mobile'
    NOTEBOOK = 'notebook'
    PC = 'pc'

    CHOICE_GROUP = {
        (MOBILE, 'mobile'),
        (NOTEBOOK, 'notebook'),
        (PC, 'pc'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=MOBILE)
    img = models.ImageField(default='no_image.jpg', upload_to='pr/')

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    MARKS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(User, models.CASCADE)
    text = models.TextField(max_length=1024)
    mark = models.IntegerField(choices=MARKS)
    product = models.ForeignKey('Product', models.CASCADE)

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    product = models.ForeignKey('Product', models.CASCADE, related_name='prod')

    def __str__(self):
        return f'{self.user}:{self.product}'
