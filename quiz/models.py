from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Category Name")
    
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural="Categories"


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20,verbose_name="Quiz title")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title