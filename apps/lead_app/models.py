# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
#for email regex
import re 
import os
EMAIL_REGEX = re.compile (r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')

class LeadManager(models.Manager):
    def leadVal(self, post, user_id):
        errors = []
        first_name = post['first_name']
        last_name = post['last_name']
        phone_number = post['phone_number']
        email = post['email']
        if len(first_name) < 3:
            errors.append('First name must be more than 3 characters')
        elif len(first_name) > 30:
            errors.append('First name must be less than 30 characters')
        if len(last_name) < 3:
            errors.append('Last name must be more than 3 characters')
        elif len(last_name) > 30:
            errors.append('Last name must be less than 30 characters')
        if len(phone_number) != 12:
            errors.append('Phone number is invalid')
        if len(email) < 1:
            errors.append('Email must be filled out')
        elif len(email) > 50:
            errors.append('Email too long')
        elif not EMAIL_REGEX.match(post['email']):
            errors.append("Invalid Email Address!")
        return {'status': len(errors) == 0, 'errors':errors}
    def createLead(self, post, user_id):
        user = User.objects.get(id = user_id)
        first_name = post['first_name']
        last_name = post['last_name']
        phone_number = post['phone_number']
        email = post['email']
        lead = self.create(first_name = first_name, last_name = last_name, phone_number = phone_number, email = email, user = user)

    def addFavorite(self, user_id, lead_id):
        lead = Lead.objects.get(id = lead_id)
        print  "this is the lead I'm trying to add", lead
        user = User.objects.get(id = user_id)
        print "this is the user", user
        lead.agent = user
        lead.save()
        print "this is the leads agent", lead.agent
        # adding to attribute not class!!!! lead.agent.add, NOT lead.add

    def removeFavorite(self, user_id, lead_id):
        lead = Lead.objects.get(id = lead_id)
        if lead:
            lead.agent = None
        lead.save()

    def deleteLead(self, lead_id):
        leadToDelete = self.filter        
        leadToDelete.delete


    def editLead(self, post, lead_id): 
        errors = []
        edit = self.get(id = lead_id)
        first_name = post['first_name']
        last_name = post['last_name']
        phone_number = post['phone_number']
        email = post['email']
        lead_id = post['lead_id']
        print "set variables"
        if len(first_name) > 2:
            print "met condition"
            if len(first_name) > 30:
                errors.append('First name must be less than 30 characters')
            else: 
                edit.first_name = first_name
                print "changed first_name"
        if len(last_name) > 2:
            if len(last_name) > 30:
                errors.append('Last name must be less than 30 characters')
            else: 
                edit.last_name= last_name
        if len(phone_number) > 2:
            if len(phone_number) != 12:
                errors.append('Phone number is invalid')
            else: 
                edit.phone_number = phone_number
        if len(email) > 2:
            if len(email) > 50:
                errors.append('Email too long')
            elif not EMAIL_REGEX.match(post['email']):
                errors.append("Invalid Email Address!")
            else: 
                edit.email = email
        edit.save()
        print edit
        return {'status': len(errors) == 0, 'errors':errors}
        

class Lead(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name = "leads")
    agent = models.ForeignKey(User, related_name = "agent_favorites", null=True)
    # null = True means "allow null; null is ok"
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LeadManager()

    def __str__(self):
        return "first_name: {}, last_name: {}, phone_number: {}, email:{}, user:{}, notes:{}, agent: {}".format(self.first_name, self.last_name, self.phone_number, self.email, self.user, self.notes, self.agent)
class NoteManager(models.Manager):
    def createNote(self, post, lead_id, user_id):
        content = post['content']
        print "stored content"
        lead = Lead.objects.get(id = lead_id)
        user = User.objects.get(id = user_id)
        note = Note.objects.create(content = content, lead = lead, user = user)

class Note(models.Model):
    content = models.CharField(max_length = 255)
    lead = models.ForeignKey(Lead, related_name = "notes")
    user = models.ForeignKey(User, related_name = "notes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = NoteManager()

# class FavoriteManager(models.Manager):
#     def createFavorite(self, lead_id, user_id):
#         lead = Lead.objects.get(id = lead_id)
#         user = User.objects.get(id = user_id)
#         Favorite = Favorite.objects.create(lead = lead, user = user)

# class Favorite(models.Model):
#     lead = models.OneToOneField(
#         lead,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         )
#     user = models.ForeignKey(User, related_name = "favoriting_users")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = FavoriteManager()

def __str__(self):
    return "content: {}, lead: {}, user: {}".format(self.content, self.lead, self.user)
# Create your models here.
