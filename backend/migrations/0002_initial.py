# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table(u'backend_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('father', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('present_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('permanent_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parents_income', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['backend.Income'])),
            ('mother_job', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('father_job', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['backend.Income'])),
            ('primary_school', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('primary_medium', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('primary_marks', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('primary_division', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('primary_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('intermediate_subjects', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('intermediate_college', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('intermediate_medium', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('intermediate_marks', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('intermediate_division', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('intermediate_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('degree_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.DegreeSubject'])),
            ('degree_college', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('degree_medium', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('degree_marks', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('degree_division', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('degree_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('degree_current_year', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('post_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.PostgraduateSubject'])),
            ('post_university', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_medium', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('post_marks', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('post_division', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('post_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('post_current_year', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('academic_distinction', self.gf('django.db.models.fields.TextField')()),
            ('essay', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'backend', ['Application'])

        # Adding model 'Income'
        db.create_table(u'backend_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lower_bound', self.gf('django.db.models.fields.IntegerField')()),
            ('upper_bound', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'backend', ['Income'])

        # Adding model 'DegreeSubject'
        db.create_table(u'backend_degreesubject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'backend', ['DegreeSubject'])

        # Adding model 'PostgraduateSubject'
        db.create_table(u'backend_postgraduatesubject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'backend', ['PostgraduateSubject'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table(u'backend_application')

        # Deleting model 'Income'
        db.delete_table(u'backend_income')

        # Deleting model 'DegreeSubject'
        db.delete_table(u'backend_degreesubject')

        # Deleting model 'PostgraduateSubject'
        db.delete_table(u'backend_postgraduatesubject')


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
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mother_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parents_income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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