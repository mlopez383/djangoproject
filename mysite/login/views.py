from django.http import HttpResponseRedirect
import time

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def check(request):
    if 'user' not in request.session:
        return True
    else:
        #if the inactividad is more 15 minutes, the system ask for a new loguin
        if int(time.time()) > request.session['user']['starttime']+54000:
            return True
        else:
            request.session['user']['starttime'] = int(time.time())
    request.session['user']['titleh'] = 'Django Project'
    return False