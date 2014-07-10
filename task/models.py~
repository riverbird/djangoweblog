from django.db import models
from datetime import datetime

# Create your models here.
class Context(models.Model):
	name = models.CharField('context',max_length=200)
	user_id = models.IntegerField(default=1)
	class Admin:
		pass
class Type(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		 return self.name
	class Admin:
		pass
class Task(models.Model):
	'''
	TYPE_CHOICES = (
			('im','Imediately'),
			('ma','Maybe'),
			('wa','Wating'),
			('id','Idea'),
			('do','Done'),
		)
	'''	
	name = models.CharField('name',max_length=200)
	description = models.TextField()
	#type = models.CharField(max_length=2,choices=TYPE_CHOICES)
	type = models.ForeignKey(Type)
	url = models.CharField(max_length=200,null=True,blank=True)
	created_on = models.DateTimeField(default=datetime.now())
	edited_on = models.DateTimeField(default=datetime.now())
	completed_on = models.DateTimeField(default=datetime.now())
	project_id = models.IntegerField()
	sort_order = models.IntegerField(default=0)
	file = models.CharField(max_length = 150,blank=True)
	status = models.IntegerField(default=0)
	user_id = models.IntegerField(default=0)
	class Admin:
		pass
class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	created_on = models.DateTimeField()
	status = models.IntegerField()
	user_id = models.IntegerField()
	class Admin:
		pass
