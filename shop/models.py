from django.db import models

# Create your models here.
class Category(models.Model):
    slug=models.SlugField(unique=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    slug=models.SlugField(unique=True)
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, related_name='subcategories',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    slug=models.SlugField(unique=True)
    name=models.CharField(max_length=100)
    subcategory =models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
        


    
        
                        