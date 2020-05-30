from django.db import models

CATEGORY_CHOICES = [('other', 'Other'), ('tech', 'Technology'), ('books', 'Books'), ('food', 'Food')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, verbose_name='Description')
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Category')
    count = models.IntegerField(null=False, blank=False, verbose_name='Count')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name='Price')
