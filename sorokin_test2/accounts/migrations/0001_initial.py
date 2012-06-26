# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('accounts_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('accounts', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('accounts_profile')


    models = {
        'accounts.profile': {
            'Meta': {'object_name': 'Profile'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['accounts']