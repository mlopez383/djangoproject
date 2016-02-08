from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import User, Privilege
import time
from datetime import datetime

def init(request):
    serror = ""
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        try:
            user = User.objects.get(login=request.POST['username'], password=request.POST['password'])
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
            serror = "The username or password are incorrect."

    context = {'request': request, 'serror':serror}
    return render(request, 'home/index.html', context)
