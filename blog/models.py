from django.db import models
from datetime import datetime

from django import forms
#from django.contrib.models import FlatPage

#from tinymce.widgets import TinyMCE
#from demo.tinymce.widgets import TinyMCE
#from tinymce import models as tinymce_models
#from demo.tinymce import models as tinymce_models
#from demo.tinymce.models import HTMLField

from django.forms import Form
from django.forms.widgets import Textarea
from django.forms.fields import CharField
from django.shortcuts import render_to_response

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=32)
	def __unicode__(self):
		return self.name
	class Admin:
		pass

class Article(models.Model):
	title         = models.CharField(max_length=64)
	published_at  = models.DateTimeField('date published')
	content       = models.TextField()
	#content       = HTMLField()
	#content = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	category      = models.ForeignKey(Category)
	def __unicode__(self):
		return self.title
	#def get_absolute_url(self):
	#	return '/feed/%i/' % self.id
	class Admin:
	#class Media:
		js = (
			'/media/js/tiny_mce/tiny_mce.js',
			'/media/js/textareas.js',
		     )
class User(models.Model):
	username = models.CharField('user name',max_length=24,unique=True)
	passowrd = models.CharField('pass word',max_length=24)
	sex = models.CharField('gender',choices=(('M','Male'),('F','Femail')),max_length=1)
	email = models.CharField('Email',max_length=64)
class Comment(models.Model):
	text = models.TextField()
	published_at = models.DateTimeField(default = datetime.now())
	article_id = models.IntegerField()
	class Admin:
		pass
