#from django.contrib.syndication.feeds import Feed
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from demo.blog.models import Article

class LastestEntries(Feed):
	feed_type = Rss201rev2Feed
	title = "Djangoweblog news"
	link = "/feeds/"
	description = "http://riverbird2005.cublog.cn"
	def items(self):
		return Article.objects.order_by('-published_at')
	def item_link(self,item):
		return "http://localhost:8000/article/%d/" % item.id
