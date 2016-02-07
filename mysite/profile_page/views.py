from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from users.models import User
from profile_page.models import Profile

def index(request):
	user = get_object_or_404(User, id=request.session['user']['userid'])
	profile = Profile.objects.get(id=user.id)

	saved = False
	if request.method == 'POST':
		user.login = request.POST['username']
		user.email = request.POST['email']
		user.save()
		profile.name = request.POST['name'];
		profile.surname = request.POST['surname'];
		profile.address = request.POST['address'];
		profile.city = request.POST['city'];
		profile.postal_code = request.POST['postal_code'];
		profile.phone = request.POST['phone'];
		profile.save()
		saved = True;


	template = loader.get_template('profile/index.html')
	context = {
		'sesion': request.session['user'],
		'user': user,
		'profile': profile,
		'saved': saved
	}
	return HttpResponse(template.render(context, request))
