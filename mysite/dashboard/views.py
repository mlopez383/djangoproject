from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {
        'sesion': request.session['user']
    }
    return HttpResponse(template.render(context, request))
