# Create your views here.
from django.template import Context,loader
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.db.models import Q
from datetime import datetime

'''
from  demo.custom_widgets import TinyMCE
from django.newforms import Form
from django.newforms.widgets import Textarea
from django.newforms.fields import CharField
from django.shortcuts import render_to_response
'''

from demo.blog.models import Article
from demo.blog.models import Category
from demo.blog.models import Comment
def index(request):
	#return HttpResponse("Hello")
	art_list = Article.objects.all().order_by('-published_at')[:5]
	category_list = Category.objects.all()
	art_cnt = Article.objects.all().count()
	page_cnt = art_cnt / 5 
	if page_cnt % 5 != 0:
		page_cnt += 1
	lst_page = [x*1 for x in range(1,page_cnt+1)]
	return render_to_response('colorimetry/index.html',
			{'art_list':art_list,
			'category_list':category_list,
			'art_cnt':art_cnt,
			'lst_page':lst_page,
			})
	'''
	output = ','.join([p.title for p in art_list])
	return HttpResponse(output)
	
	t = loader.get_template('colorimetry/article_list.html')
	c = Context({
		'art_list':art_list,
		})
	return HttpResponse(t.render(c))
	'''
def detail(request,art_id):
	#return HttpResponse("detail: %s." % art_id)
	try:
		art = Article.objects.get(id=art_id)
	except Article.DoesNotExist:
		raise Http404
	try:
		comm = Comment.objects.filter(article_id = art_id).order_by('-published_at')
	except Comment.DoesNotExist:
		raise Http404
	return render_to_response('colorimetry/article.html',{'art':art,
		'comm':comm,})
def page(request,page_id):
	category_list = Category.objects.all()
	n_page_id = int(page_id)
	n_end = n_page_id * 5
	n_start = n_end - 5
	page_list = Article.objects.all().order_by('-published_at')[n_start:n_end]
	art_cnt = Article.objects.all().count()
	page_cnt = art_cnt / 5 
	if page_cnt % 5 != 0:
		page_cnt += 1
	lst_page = [x*1 for x in range(1,page_cnt+1)]
	return render_to_response('colorimetry/page.html',
			{'page_list':page_list,
			'category_list':category_list,
			'art_cnt':art_cnt,
			'lst_page':lst_page,
			})

	#return render_to_response('colorimetry/article.html',{'pages':pages,})
def search(request):
	query = request.GET.get('s',"")
	if query:
		results = Article.objects.extra(where=['title like %s'],params=['%' + query + '%'])
		total = results.count()
	else:
		results = []
	return render_to_response("colorimetry/search.html",{"results":results,"query":query,"total":total,})
	'''
	if request.POST:
		return render_to_response('colorimetry/search.html',{'result':demo(request.POST['term'],10)})
		print request.POST['term']
		return HttpResponseRedirect("/")
	else:
		return render_to_response("search.html")
	'''
def cate(request,cate_id):
	#return HttpResponse("detail: %s." % art_id)
	try:
		art_list = Article.objects.filter(category = cate_id).order_by('-published_at')
	except Article.DoesNotExist:
		raise Http404
	category_list = Category.objects.all()
	art_cnt = Article.objects.all().count()
	page_cnt = art_cnt / 5 
	if page_cnt % 5 != 0:
		page_cnt += 1
	lst_page = [x*1 for x in range(1,page_cnt+1)]
	return render_to_response('colorimetry/index.html',
			{'art_list':art_list,
			'category_list':category_list,
			'art_cnt':art_cnt,
			'lst_page':lst_page,
			})
def sendcomment(request,art_id):
	if request.POST.has_key('txt_comment'):
		get_comment = request.POST.get('txt_comment','none')
		new_comment = Comment(text = get_comment,article_id = art_id,published_at = datetime.now())
		new_comment.save()
	return HttpResponseRedirect('/article/%s' % art_id)
