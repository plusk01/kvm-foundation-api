# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Application.permanent_address'
        db.alter_column(u'backend_application', 'permanent_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Application.occupation'
        db.alter_column(u'backend_application', 'occupation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.income'
        db.alter_column(u'backend_application', 'income_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['backend.Income']))

    def backwards(self, orm):

        # Changing field 'Application.permanent_address'
        db.alter_column(u'backend_application', 'permanent_address', self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 4, 3, 0, 0), max_length=255))

        # Changing field 'Application.occupation'
        db.alter_column(u'backend_application', 'occupation', self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 4, 3, 0, 0), max_length=100))

        # Changing field 'Application.income'
        db.alter_column(u'backend_application', 'income_id', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 4, 3, 0, 0), to=orm['backend.Income']))

    models = {
        u'backend.application': {
            'Meta': {'object_name': 'Application'},
            'academic_distinction': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'degree_college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'degree_current_year': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'degree_division': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'degree_marks': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'degree_medium': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'degree_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'degree_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.DegreeSubject']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'essay': ('django.db.models.fields.TextField', [], {}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'father_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['backend.Income']"}),
            'intermediate_college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'intermediate_division': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'intermediate_marks': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'intermediate_medium': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'intermediate_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'intermediate_subjects': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'is_employed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_looking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_student': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mother_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'parents_income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_current_year': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'post_division': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'post_marks': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'post_medium': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'post_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'post_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.PostgraduateSubject']"}),
            'post_university': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'present_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_division': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'primary_marks': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'primary_medium': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'primary_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'primary_school': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'backend.degreesubject': {
            'Meta': {'object_name': 'DegreeSubject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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