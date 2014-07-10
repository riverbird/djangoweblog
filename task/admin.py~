from demo.task.models import Context 
from demo.task.models import Task
from demo.task.models import Project
from demo.task.models import Type
from django.contrib import admin
class TypeAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,{'fields':['name']}),
			]
	search_fields = ['name']
	list_display = ('name',)
class ContextAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,{"fields":["name"]}),
			]
	search_fields = ['name']
	list_display = ('name',)
class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,{'fields':['name']}),
			(None,{'fields':['project_id']}),
			(None,{'fields':['description']}),
			(None,{'fields':['url']}),
			(None,{'fields':['type']}),
			]
	search_fields=['name']
	list_display = ('name','type',)
class ProjectAdmin(admin.ModelAdmin):
	fielsets = [
			(None,{'fields':['name']}),
			]
	search_fields = ['name']
	list_display = ('name','description',)
admin.site.register(Context,ContextAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Type,TypeAdmin)
