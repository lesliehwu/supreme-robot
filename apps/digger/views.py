# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = ''
    return render(request, 'index.html')

def process(request):
    if request.GET['building'] == 'farm':
        added = random.randint(10,21)
        request.session['gold'] += added
        action = '\nEarned ' + str(added) + ' golds from the farm! (' + str(datetime.now()) + ')'
        request.session['activity'] += action

    if request.GET['building'] == 'cave':
        added = random.randint(5,11)
        request.session['gold'] += added
        action = '\nEarned ' + str(added) + ' golds from the cave! (' + str(datetime.now()) + ')'
        request.session['activity'] += action

    if request.GET['building'] == 'house':
        added = random.randint(2,6)
        request.session['gold'] += added
        action ='\n Earned ' + str(added) + ' golds from the house! (' + str(datetime.now()) + ')'
        request.session['activity'] += action

    if request.GET['building'] == 'casino':
        added = random.randint(-50,51)
        request.session['gold'] += added
        if added >= 0 :
            action = '\nEarned ' + str(added) + ' golds from the casino! (' + str(datetime.now()) + ')'
        else:
            action='\nLost ' + str(added) + ' golds from the casino! (' + str(datetime.now()) + ')'
        request.session['activity'] += action
        
    return redirect('/')
