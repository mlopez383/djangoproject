from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import User, Privilege
import time
from datetime import datetime

def login(request):
    serror = ""
    if request.method == 'POST' and 'inputEmail' in request.POST and 'inputPassword' in request.POST:
        try:
            user = User.objects.get(login=request.POST['inputEmail'], password=request.POST['inputPassword'])
            request.session['user'] = {}
            request.session['user']['userid'] = user.id
            request.session['user']['userlogin'] = user.login
            request.session['user']['userprivilege'] = user.privilege.id
            request.session['user']['starttime'] = int(time.time())

            if request.session['user']['userprivilege'] != 1 and request.session['user']['userprivilege'] != 2:
                return HttpResponseRedirect('/')

            user.last_visit_date = datetime.now()
            user.save()
            return HttpResponseRedirect('/dashboard/')
        except User.DoesNotExist:
            serror = "El nombre de user ingresado no existe o el password asociado a el es incorrecto."

    context = {'request': request, 'serror':serror}
    return render(request, 'login/index.html', context)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')
