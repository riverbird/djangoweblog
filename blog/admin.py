from demo.blog.models import Article
from demo.blog.models import Category
from demo.blog.models import User
from demo.blog.models import Comment
from django.contrib import admin
class ArticleAdmin(admin.ModelAdmin):
	#fields = ['title','published_at']
	search_fields = ['title']
	list_filter = ['category']
	class Media:
	        js = (
		     '/media/js/tiny_mce/tiny_mce.js',
		     '/media/js/textareas.js',
		)

class CategoryAdmin(admin.ModelAdmin):
	search_fields=['name']
class UserAdmin(admin.ModelAdmin):
	search_fields=['username']
class CommentAdmin(admin.ModelAdmin):
	search_fields=['text']
	list_display = ('text','article_id',)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User,UserAdmin)

