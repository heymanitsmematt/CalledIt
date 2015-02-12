from app.models import *
from api.Odds import *
import requests
from __future__ import absolute_import

from celery import shared_task

@shared_task
def updateOdds():
    r = requests.post('http://192.168.56.101/api/updateOdds/')
