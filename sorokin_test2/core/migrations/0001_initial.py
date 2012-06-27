# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('core_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('status_code', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('params', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('core_request')


    models = {
        'core.request': {
            'Meta': {'object_name': 'Request'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'params': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'status_code': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['core']