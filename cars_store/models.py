from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Goods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='goods/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    