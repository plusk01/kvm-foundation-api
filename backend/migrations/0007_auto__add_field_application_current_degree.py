# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Application.current_degree'
        db.add_column(u'backend_application', 'current_degree',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['backend.DegreeType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Application.current_degree'
        db.delete_column(u'backend_application', 'current_degree_id')


    models = {
        u'backend.application': {
            'Meta': {'object_name': 'Application'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'current_degree': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.DegreeType']"}),
            'current_degree_user': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'current_subjects': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'current_year': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'essay': ('django.db.models.fields.TextField', [], {}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'father_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mother_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parents_income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'present_address': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'backend.degreesubject': {
            'Meta': {'object_name': 'DegreeSubject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'backend.degreetype': {
            'Meta': {'object_name': 'DegreeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'backend.income': {
            'Meta': {'object_name': 'Income'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lower_bound': ('django.db.models.fields.IntegerField', [], {}),
            'upper_bound': ('django.db.models.fields.IntegerField', [], {})
        },
        u'backend.postgraduatesubject': {
            'Meta': {'object_name': 'PostgraduateSubject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['backend']