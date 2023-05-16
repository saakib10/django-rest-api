from django.db import models

class Author(models.Model):
    
    name = models.CharField(max_length=30,null=False)
    address = models.CharField(max_length=50,null=False,default="Dhaka")
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=False)
    headline = models.CharField(max_length=30,null=False)
    context = models.TextField(null=False)
