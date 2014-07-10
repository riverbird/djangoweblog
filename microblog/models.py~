from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
	published_at  = models.DateTimeField(default=datetime.now())
	content       = models.TextField()
	def __unicode__(self):
		return self.content
	class Admin:
		pass
