from django.shortcuts import render, render_to_response
from app.models import User, Sport, Event, Party, Prediction
from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponse
import simplejson
from django.views.decorators.csrf import csrf_exempt
from clTroller import Troller
from django.core import serializers
from django.template import RequestContext, loader
import requests


class NAABBall(View)
    
