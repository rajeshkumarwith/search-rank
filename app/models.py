from django.db import models

# Create your models here.
class DBSStorage(models.Model):
    id=models.IntegerField(primary_key=True)
    query=models.CharField(max_length=200, unique=True)
    rank=models.IntegerField()
    link=models.CharField(max_length=200, unique=True)
    title=models.CharField(max_length=200,blank=True, null=True)
    snippet=models.CharField(max_length=200,blank=True,null=True)
    html=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.query)
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title