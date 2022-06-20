from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    product = models.CharField(max_length=200)
    order_date = models.DateField()


    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return f'/order/{self.pk}'
