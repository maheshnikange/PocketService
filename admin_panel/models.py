from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='test.png' , upload_to='uploads/category_images/')

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(default='test.png' ,upload_to='uploads/service_images/')

    def get_category_name(self):
        return self.category.name

class Advertise(models.Model):
    image = models.ImageField(upload_to='uploads/advertise_images/')
    image_type = models.CharField(max_length=100, default= 'static')
    location = models.CharField(max_length=100, null=True, default='main')
