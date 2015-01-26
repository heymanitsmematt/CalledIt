from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import simplejson
from django.core import serializers
from django.template import RequestContext, loader
from django.views.generic import ListView, View, TemplateView, FormView
from models import User, Sport, Team, Event, Party, Prediction, Tournament
from app.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
	return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class Main(LoggedInMixin, TemplateView):
    model = Sport
    template_name = "app/main.html"
    
    def head(self, *args, **kwargs):
	predictions = Prediction.objects.all()
	response = HttpResponse('')
	response['predictions'] = predictions
        return response 
    def get_context_data(self, **kwargs):
	context = super(Main, self).get_context_data(**kwargs)
	context.update({'request': self.request, 'user': self.request.user, 'sport' : Sport.objects.all(), 'tournaments' : Tournament.objects.all(), 'pendingEvents' : Event.objects.exclude(eventDate__isnull=True)})
	return context
	
	

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method =='POST':
	user_form = UserForm(data=request.POST)
	profile_form = UserProfile(data=request.POST)

	if user_form.is_valid() and profile_form.is_valid():
	    user = user_form.save()
	    user.set_password(user.password)
	    user.save()

	    profile = profile_form.save(commit=False)
	    profile.user = user

	    if 'picture' in request.FILES:
		profile.picture = request.FILES['picture']
	    if 'rating' in request.POST:
		profile.rating = request.POST['rating']
	
	    profile.save()
	    registered = True
	else:
	    print user_form.errors, profile_form.errors

    else:
	user_form = UserForm()
	profile_form = UserProfileForm()

    return render_to_response('app/register.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered}, context)

