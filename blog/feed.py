from django.contrib.syndication.feeds import Feed
from demo.blog.models import Article

class LatestEntries(Feed):
	title = "Djangoweblog news"
	link = "/feeds/"
	description = "http://riverbird2005.cublog.cn"
	def items(self):
		return Article.objects.order_by('-published_at')
