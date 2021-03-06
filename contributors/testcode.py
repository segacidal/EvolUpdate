__author__ = 'christopherjenness'

from django.db import models
import datetime
from django.utils import timezone

class HaveYouSeen(models.Model):
    theirtitle=models.CharField('Their Title', max_length=300, blank=True)
    dateadded=models.DateTimeField('Date Added')
    mytitle=models.CharField('My Title', max_length=300, blank=True)
    reference=models.URLField(blank= True)

class ThisMonthInEvolution(models.Model):
    headline=models.CharField(max_length=300)
    summary=models.TextField()
    thismonthpic=models.ImageField('This month picture', blank=True, upload_to='ThisMonth')
    reference=models.URLField(blank=True)

class Contributor(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=1000, blank=True)
    rank=models.IntegerField(blank=True)
    description=models.TextField()
    picture=models.ImageField(blank=True, upload_to='ContribImages')
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=500)
    pub_date= models.DateTimeField('Date Published')
    reference=models.URLField(blank= True)
    subject=models.CharField(max_length=300, blank=True)
    organisms=models.CharField(max_length=300, blank=True)
    datatypes=models.CharField('Data Types', max_length=300, blank=True)
    journal=models.CharField(max_length=300, blank=True)
    summary=models.CharField(max_length=5000, blank=True)
    authors=models.CharField(max_length=5000, blank=True)
    article=models.TextField(blank=True)
    contrib = models.ForeignKey(Contributor, blank=True, null=True)
    articlepic=models.ImageField('Article Picture', blank=True, upload_to='ArticleImages')
    def __unicode__(self):
        return self.title

class Email(models.Model):
    email=models.EmailField(max_length=254)
    def __unicode__(self):
        return self.email

class Contact(models.Model):
    feedback=models.TextField(max_length=2000)
    def __unicode__(self):
        return self.feedback