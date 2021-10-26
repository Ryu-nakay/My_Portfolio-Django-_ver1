from django.db import models

# Create your models here.

#モデルはadmin.pyに追加すること！
class NewsModel(models.Model):
    title=models.CharField(max_length=80)
    contents=models.CharField(max_length=600)
    date=models.DateField()

    def __str__(self):
        return 'title:'+self.title+'contents:'+self.contents+'date:'+str(self.date)
    
class AppModel(models.Model):
    appName=models.CharField(max_length=80)
    imagePath=models.URLField(blank=True,null=True)
    googlePath=models.URLField(blank=True,null=True)
    applePath=models.URLField(blank=True,null=True)
    otherPath=models.URLField(blank=True,null=True)

    def __str__(self):
        return 'appName:'+self.appName

