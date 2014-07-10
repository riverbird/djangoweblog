# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.db.models import Q
from datetime import datetime
from demo.microblog.models import Entry

def index(request,p_id):
	entry_list = Entry.objects.all().order_by('-published_at')[:5]
	entry_cnt = Entry.objects.all().count()
	page_cnt = entry_cnt / 20
	if page_cnt % 20 != 0:
		page_cnt += 1
	lst_page = [x*1 for x in range(1,page_cnt+1)]
	return render_to_response('exposure/index.html',
		{'entry_list':entry_list,
		'entry_cnt':entry_cnt,
		'lst_page':lst_page,})
def send(request):
	#new_entry = Entry(content = "I'm zhanghong!")
	#new_entry.save()
	if request.POST.has_key('t'):
		entry_content = request.POST.get('t','none')
		#entry_content = request.POST['t']
		new_entry = Entry(content = entry_content,published_at=datetime.now())
		new_entry.save()
		return HttpResponseRedirect('/microblog/1')
	'''
	#used get method
	query = request.GET.get('t',"")
	if query:
		new_entry = Entry(content = query)
		new_entry.save()
	entry_list = Entry.objects.all().order_by('-published_at')[:15]
	return render_to_response("exposure/index.html",{"entry_list":entry_list,"query":query,})
	'''
