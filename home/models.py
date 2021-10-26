from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=80)
    contents=models.CharField(max_length=600)
    date=models.DateField()

    def __str__(self):
        return 'title:'+self.title+'contents:'+self.contents+'date:'+self.date
    