# Create your views here.
from polls.models import Poll
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
	
from polls.models import Poll
from django.http import HttpResponse

"""
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	output = ', '.join([p.question for p in latest_poll_list])
	return HttpResponse(output)
"""
	
from django.shortcuts import render_to_response

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render_to_response('polls/index.html', context)
	
from django.http import Http404
# ...
def detail(request, poll_id):
	try:
		p = Poll.objects.get(id=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render_to_response('polls/detail.html', {'poll': p})

from django.template import RequestContext
# ...
def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

