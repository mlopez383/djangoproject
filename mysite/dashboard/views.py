from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from login.views import check

def index(request):
	if check(request):
		return HttpResponseRedirect('/logout/')

	template = loader.get_template('dashboard/index.html')
	context = {
		'sesion': request.session['user']
	}
	return HttpResponse(template.render(context, request))
