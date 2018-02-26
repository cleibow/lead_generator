# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import Lead
from models import Note
from ..login_app.models import User

def index(request):
    user_id = request.session['user_id']
    currentUser = User.objects.get(id = user_id)
    mine = currentUser.leads.values_list('id', flat = True)
    if currentUser.agent == "true":
        leadList = currentUser.agent_favorites.values_list('id', flat = True)
        myLeads = Lead.objects.exclude(id__in=leadList)   
    else: 
        myLeads = Lead.objects.filter(id__in=mine)
    print myLeads
    data = {
        'leads': myLeads,
        'user': currentUser
    }
    return render(request, 'lead_app/index.html', data)


def renderNewLead(request):
    data = {
        'user_id': request.session['user_id']
    }
    user_id = request.session['user_id']
    return render(request, 'lead_app/new_lead.html', data)

def addLead(request):
    #post is in REQUEST, so dont need to add user_id here
    if 'user_id' not in request.session:
            return redirect('/')
    user_id = request.session['user_id']
    res = Lead.objects.leadVal(request.POST, user_id)
    print res
    if res['status']: 
        lead = Lead.objects.createLead(request.POST, request.session['user_id'])
    else:
        for error in res['errors']:
            messages.error(request, error)
        print res['errors']
    return redirect('/leads/create')

def favoriteLead(request, lead_id):
    user_id = request.session['user_id']
    # Lead.agent.add(user)
    Lead.objects.addFavorite(user_id, lead_id)
    return redirect('/leads/favorites')

def deleteFav(request, lead_id):
    user_id = request.session['user_id']
    Lead.objects.removeFavorite(user_id, lead_id)
    return redirect('/leads/favorites')

def renderFav(request):
    currentUser = User.objects.get(id = request.session['user_id'])
    leadList = currentUser.agent_favorites.values_list('id', flat = True)
    myLeads = Lead.objects.filter(id__in=leadList)
    data = {
        'leads' : myLeads,
        'user': currentUser
    }
    return render(request, 'lead_app/favorite.html', data)
    
def renderEdit(request, lead_id):
    data = {
        'lead_id': lead_id
    }
    return render(request, 'lead_app/edit.html', data)

def editLead(request, lead_id):
    if 'user_id' not in request.session:
        return redirect('/')
    res = Lead.objects.editLead(request.POST, lead_id)
    print res
    if res['status'] == False:
        for error in res['errors']:
            messages.error(request, error)
        print res['errors']
        return redirect('/leads/edit/<lead_id>')
    else:
        return redirect ('/leads')

def deleteLead(request, lead_id):
    user_id = request.session['user_id']
    currentLead = Lead.objects.get(id = lead_id)
    if user_id != currentLead.user.id:
        messages.error(request, "Not created by you")
        return redirect('/leads')
    else:
        Lead.objects.deleteLead(lead_id)
        return redirect('/leads')

def leadProfile(request, lead_id):
    thisLead = Lead.objects.get(id = lead_id)
    notes = Note.objects.filter(lead = thisLead)
    data = {
        'lead': thisLead,
        'notes': notes
    }
    print thisLead.notes.all()
    print thisLead.first_name
    return render(request, 'lead_app/lead_profile.html', data)

def createNote(request, lead_id):
    user_id = request.session['user_id']
    Note.objects.createNote(request.POST, lead_id, user_id)
    print "created note"
    return redirect('/leads/view/{}'.format(lead_id))
    
    

    

# Create your views here.
