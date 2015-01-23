from django.shortcuts import render
from django.http import HttpResponse
import simplejson
from django.core import serializers
from django.template import RequestContext, loader
from django.views.generic import ListView, View, TemplateView, FormView
from models import User, Sport, Team, Event, Party, Prediction

class Main(View):
    model = Sport
