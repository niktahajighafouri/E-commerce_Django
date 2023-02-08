from django.db import models
from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.name


class Menu_item(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.IntegerField('price')
    description = models.CharField('description', max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category.name+":"+str(self.price)+":"+self.description+self.category.name

# Create your models here.
