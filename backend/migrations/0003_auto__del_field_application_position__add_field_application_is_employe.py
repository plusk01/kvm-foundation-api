# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Application.position'
        db.delete_column(u'backend_application', 'position')

        # Adding field 'Application.is_employed'
        db.add_column(u'backend_application', 'is_employed',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.is_looking'
        db.add_column(u'backend_application', 'is_looking',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.is_student'
        db.add_column(u'backend_application', 'is_student',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Application.position'
        db.add_column(u'backend_application', 'position',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 4, 3, 0, 0), max_length=1),
                      keep_default=False)

        # Deleting field 'Application.is_employed'
        db.delete_column(u'backend_application', 'is_employed')

        # Deleting field 'Application.is_looking'
        db.delete_column(u'backend_application', 'is_looking')

        # Deleting field 'Application.is_student'
        db.delete_column(u'backend_application', 'is_student')


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
            'income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
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
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parents_income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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