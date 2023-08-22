from django.db import models

# Create your models here.
class place(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics',blank=True)
    des=models.TextField()
class world(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='wats',blank=True)
    des=models.TextField()
class travel(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='trl',blank=True)
    des=models.TextField()

class person(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='name1',blank=True)
    des=models.TextField()



    def __str__(self):
        return self.name
