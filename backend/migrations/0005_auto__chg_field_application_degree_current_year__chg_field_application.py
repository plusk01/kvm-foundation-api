# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Application.degree_current_year'
        db.alter_column(u'backend_application', 'degree_current_year', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.intermediate_medium'
        db.alter_column(u'backend_application', 'intermediate_medium', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Application.post_division'
        db.alter_column(u'backend_application', 'post_division', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.intermediate_division'
        db.alter_column(u'backend_application', 'intermediate_division', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.intermediate_marks'
        db.alter_column(u'backend_application', 'intermediate_marks', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_medium'
        db.alter_column(u'backend_application', 'degree_medium', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Application.post_medium'
        db.alter_column(u'backend_application', 'post_medium', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Application.post_marks'
        db.alter_column(u'backend_application', 'post_marks', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_passing'
        db.alter_column(u'backend_application', 'degree_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'Application.degree_marks'
        db.alter_column(u'backend_application', 'degree_marks', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Application.primary_medium'
        db.alter_column(u'backend_application', 'primary_medium', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Application.intermediate_passing'
        db.alter_column(u'backend_application', 'intermediate_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'Application.primary_school'
        db.alter_column(u'backend_application', 'primary_school', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.post_passing'
        db.alter_column(u'backend_application', 'post_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'Application.post_university'
        db.alter_column(u'backend_application', 'post_university', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.intermediate_college'
        db.alter_column(u'backend_application', 'intermediate_college', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.degree_division'
        db.alter_column(u'backend_application', 'degree_division', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.degree_college'
        db.alter_column(u'backend_application', 'degree_college', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.primary_division'
        db.alter_column(u'backend_application', 'primary_division', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.post_current_year'
        db.alter_column(u'backend_application', 'post_current_year', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Application.primary_passing'
        db.alter_column(u'backend_application', 'primary_passing', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'Application.intermediate_subjects'
        db.alter_column(u'backend_application', 'intermediate_subjects', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Application.primary_marks'
        db.alter_column(u'backend_application', 'primary_marks', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_subject'
        db.alter_column(u'backend_application', 'degree_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.DegreeSubject'], null=True))

        # Changing field 'Application.post_subject'
        db.alter_column(u'backend_application', 'post_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.PostgraduateSubject'], null=True))

        # Changing field 'Application.academic_distinction'
        db.alter_column(u'backend_application', 'academic_distinction', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Application.degree_current_year'
        db.alter_column(u'backend_application', 'degree_current_year', self.gf('django.db.models.fields.CharField')(default=2, max_length=2))

        # Changing field 'Application.intermediate_medium'
        db.alter_column(u'backend_application', 'intermediate_medium', self.gf('django.db.models.fields.CharField')(default=2, max_length=1))

        # Changing field 'Application.post_division'
        db.alter_column(u'backend_application', 'post_division', self.gf('django.db.models.fields.CharField')(default=2, max_length=2))

        # Changing field 'Application.intermediate_division'
        db.alter_column(u'backend_application', 'intermediate_division', self.gf('django.db.models.fields.CharField')(default=2, max_length=2))

        # Changing field 'Application.intermediate_marks'
        db.alter_column(u'backend_application', 'intermediate_marks', self.gf('django.db.models.fields.DecimalField')(default=2, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_medium'
        db.alter_column(u'backend_application', 'degree_medium', self.gf('django.db.models.fields.CharField')(default=2, max_length=1))

        # Changing field 'Application.post_medium'
        db.alter_column(u'backend_application', 'post_medium', self.gf('django.db.models.fields.CharField')(default=2, max_length=1))

        # Changing field 'Application.post_marks'
        db.alter_column(u'backend_application', 'post_marks', self.gf('django.db.models.fields.DecimalField')(default=2, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_passing'
        db.alter_column(u'backend_application', 'degree_passing', self.gf('django.db.models.fields.IntegerField')(default=2, max_length=4))

        # Changing field 'Application.degree_marks'
        db.alter_column(u'backend_application', 'degree_marks', self.gf('django.db.models.fields.DecimalField')(default=2, max_digits=4, decimal_places=2))

        # Changing field 'Application.primary_medium'
        db.alter_column(u'backend_application', 'primary_medium', self.gf('django.db.models.fields.CharField')(default=2, max_length=1))

        # Changing field 'Application.intermediate_passing'
        db.alter_column(u'backend_application', 'intermediate_passing', self.gf('django.db.models.fields.IntegerField')(default=2, max_length=4))

        # Changing field 'Application.primary_school'
        db.alter_column(u'backend_application', 'primary_school', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))

        # Changing field 'Application.post_passing'
        db.alter_column(u'backend_application', 'post_passing', self.gf('django.db.models.fields.IntegerField')(default=2, max_length=4))

        # Changing field 'Application.post_university'
        db.alter_column(u'backend_application', 'post_university', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))

        # Changing field 'Application.intermediate_college'
        db.alter_column(u'backend_application', 'intermediate_college', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))

        # Changing field 'Application.degree_division'
        db.alter_column(u'backend_application', 'degree_division', self.gf('django.db.models.fields.CharField')(default=22, max_length=2))

        # Changing field 'Application.degree_college'
        db.alter_column(u'backend_application', 'degree_college', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))

        # Changing field 'Application.primary_division'
        db.alter_column(u'backend_application', 'primary_division', self.gf('django.db.models.fields.CharField')(default=2, max_length=2))

        # Changing field 'Application.post_current_year'
        db.alter_column(u'backend_application', 'post_current_year', self.gf('django.db.models.fields.CharField')(default=2, max_length=2))

        # Changing field 'Application.primary_passing'
        db.alter_column(u'backend_application', 'primary_passing', self.gf('django.db.models.fields.IntegerField')(default=2, max_length=4))

        # Changing field 'Application.intermediate_subjects'
        db.alter_column(u'backend_application', 'intermediate_subjects', self.gf('django.db.models.fields.CharField')(default=2, max_length=100))

        # Changing field 'Application.primary_marks'
        db.alter_column(u'backend_application', 'primary_marks', self.gf('django.db.models.fields.DecimalField')(default=2, max_digits=4, decimal_places=2))

        # Changing field 'Application.degree_subject'
        db.alter_column(u'backend_application', 'degree_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['backend.DegreeSubject']))

        # Changing field 'Application.post_subject'
        db.alter_column(u'backend_application', 'post_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['backend.PostgraduateSubject']))

        # Changing field 'Application.academic_distinction'
        db.alter_column(u'backend_application', 'academic_distinction', self.gf('django.db.models.fields.TextField')(default=2))

    models = {
        u'backend.application': {
            'Meta': {'object_name': 'Application'},
            'academic_distinction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'degree_college': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'degree_current_year': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'degree_division': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'degree_marks': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'degree_medium': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'degree_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'degree_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.DegreeSubject']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'essay': ('django.db.models.fields.TextField', [], {}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'father_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['backend.Income']"}),
            'intermediate_college': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'intermediate_division': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'intermediate_marks': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'intermediate_medium': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'intermediate_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'intermediate_subjects': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_employed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_looking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_student': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mother_job': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'parents_income': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['backend.Income']"}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_current_year': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'post_division': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'post_marks': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'post_medium': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'post_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'post_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.PostgraduateSubject']", 'null': 'True', 'blank': 'True'}),
            'post_university': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'present_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_division': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'primary_marks': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'primary_medium': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'primary_passing': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'primary_school': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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