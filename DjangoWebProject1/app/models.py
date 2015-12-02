"""
Definition of models.
"""

from django.db import models

# Create your models here.

class MyViewModel(models.Model):
    ad = models.CharField(max_length=200)
    soyad = models.CharField(max_length=200)
    dogumtarihi = models.DateTimeField('date published')



class Post(models.Model):
    author = models.TextField()
    text = models.TextField()

    # Time is a rhinocerous
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text+' - '+self.author.username