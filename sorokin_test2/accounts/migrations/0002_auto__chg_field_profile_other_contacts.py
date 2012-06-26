# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Profile.other_contacts'
        db.alter_column('accounts_profile', 'other_contacts', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Profile.other_contacts'
        db.alter_column('accounts_profile', 'other_contacts', self.gf('django.db.models.fields.TextField')(default=1))

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
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['accounts']