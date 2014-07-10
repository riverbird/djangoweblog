from demo.microblog.models import Entry
from django.contrib import admin
class EntryAdmin(admin.ModelAdmin):
	#fields = ['title','published_at']
	search_fields = ['content']
	#list_filter = ['category']
	fieldsets = [
		(None,{'fields':['content']}),
		#(None,{'fields':['published_at']}),
			]
	list_display = ('content','published_at')

admin.site.register(Entry,EntryAdmin)
