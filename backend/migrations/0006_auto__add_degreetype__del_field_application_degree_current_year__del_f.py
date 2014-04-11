# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DegreeType'
        db.create_table(u'backend_degreetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'backend', ['DegreeType'])

        # Deleting field 'Application.degree_current_year'
        db.delete_column(u'backend_application', 'degree_current_year')

        # Deleting field 'Application.intermediate_marks'
        db.delete_column(u'backend_application', 'intermediate_marks')

        # Deleting field 'Application.degree_medium'
        db.delete_column(u'backend_application', 'degree_medium')

        # Deleting field 'Application.post_medium'
        db.delete_column(u'backend_application', 'post_medium')

        # Deleting field 'Application.occupation'
        db.delete_column(u'backend_application', 'occupation')

        # Deleting field 'Application.post_marks'
        db.delete_column(u'backend_application', 'post_marks')

        # Deleting field 'Application.primary_medium'
        db.delete_column(u'backend_application', 'primary_medium')

        # Deleting field 'Application.intermediate_medium'
        db.delete_column(u'backend_application', 'intermediate_medium')

        # Deleting field 'Application.primary_school'
        db.delete_column(u'backend_application', 'primary_school')

        # Deleting field 'Application.is_student'
        db.delete_column(u'backend_application', 'is_student')

        # Deleting field 'Application.post_university'
        db.delete_column(u'backend_application', 'post_university')

        # Deleting field 'Application.is_looking'
        db.delete_column(u'backend_application', 'is_looking')

        # Deleting field 'Application.degree_college'
        db.delete_column(u'backend_application', 'degree_college')

        # Deleting field 'Application.degree_subject'
        db.delete_column(u'backend_application', 'degree_subject_id')

        # Deleting field 'Application.post_current_year'
        db.delete_column(u'backend_application', 'post_current_year')

        # Deleting field 'Application.primary_passing'
        db.delete_column(u'backend_application', 'primary_passing')

        # Deleting field 'Application.primary_marks'
        db.delete_column(u'backend_application', 'primary_marks')

        # Deleting field 'Application.intermediate_subjects'
        db.delete_column(u'backend_application', 'intermediate_subjects')

        # Deleting field 'Application.is_employed'
        db.delete_column(u'backend_application', 'is_employed')

        # Deleting field 'Application.post_division'
        db.delete_column(u'backend_application', 'post_division')

        # Deleting field 'Application.intermediate_division'
        db.delete_column(u'backend_application', 'intermediate_division')

        # Deleting field 'Application.degree_passing'
        db.delete_column(u'backend_application', 'degree_passing')

        # Deleting field 'Application.degree_marks'
        db.delete_column(u'backend_application', 'degree_marks')

        # Deleting field 'Application.academic_distinction'
        db.delete_column(u'backend_application', 'academic_distinction')

        # Deleting field 'Application.intermediate_passing'
        db.delete_column(u'backend_application', 'intermediate_passing')

        # Deleting field 'Application.post_passing'
        db.delete_column(u'backend_application', 'post_passing')

        # Deleting field 'Application.income'
        db.delete_column(u'backend_application', 'income_id')

        # Deleting field 'Application.intermediate_college'
        db.delete_column(u'backend_application', 'intermediate_college')

        # Deleting field 'Application.degree_division'
        db.delete_column(u'backend_application', 'degree_division')

        # Deleting field 'Application.primary_division'
        db.delete_column(u'backend_application', 'primary_division')

        # Deleting field 'Application.post_subject'
        db.delete_column(u'backend_application', 'post_subject_id')

        # Adding field 'Application.current_degree_user'
        db.add_column(u'backend_application', 'current_degree_user',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.current_year'
        db.add_column(u'backend_application', 'current_year',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.current_subjects'
        db.add_column(u'backend_application', 'current_subjects',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.institution_name'
        db.add_column(u'backend_application', 'institution_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'DegreeType'
        db.delete_table(u'backend_degreetype')

        # Adding field 'Application.degree_current_year'
        db.add_column(u'backend_application', 'degree_current_year',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_marks'
        db.add_column(u'backend_application', 'intermediate_marks',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_medium'
        db.add_column(u'backend_application', 'degree_medium',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_medium'
        db.add_column(u'backend_application', 'post_medium',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.occupation'
        db.add_column(u'backend_application', 'occupation',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_marks'
        db.add_column(u'backend_application', 'post_marks',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.primary_medium'
        db.add_column(u'backend_application', 'primary_medium',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_medium'
        db.add_column(u'backend_application', 'intermediate_medium',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.primary_school'
        db.add_column(u'backend_application', 'primary_school',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.is_student'
        db.add_column(u'backend_application', 'is_student',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_university'
        db.add_column(u'backend_application', 'post_university',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.is_looking'
        db.add_column(u'backend_application', 'is_looking',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_college'
        db.add_column(u'backend_application', 'degree_college',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_subject'
        db.add_column(u'backend_application', 'degree_subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.DegreeSubject'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_current_year'
        db.add_column(u'backend_application', 'post_current_year',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.primary_passing'
        db.add_column(u'backend_application', 'primary_passing',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.primary_marks'
        db.add_column(u'backend_application', 'primary_marks',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_subjects'
        db.add_column(u'backend_application', 'intermediate_subjects',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.is_employed'
        db.add_column(u'backend_application', 'is_employed',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_division'
        db.add_column(u'backend_application', 'post_division',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_division'
        db.add_column(u'backend_application', 'intermediate_division',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_passing'
        db.add_column(u'backend_application', 'degree_passing',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_marks'
        db.add_column(u'backend_application', 'degree_marks',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.academic_distinction'
        db.add_column(u'backend_application', 'academic_distinction',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_passing'
        db.add_column(u'backend_application', 'intermediate_passing',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_passing'
        db.add_column(u'backend_application', 'post_passing',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.income'
        db.add_column(u'backend_application', 'income',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['backend.Income'], blank=True),
                      keep_default=False)

        # Adding field 'Application.intermediate_college'
        db.add_column(u'backend_application', 'intermediate_college',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.degree_division'
        db.add_column(u'backend_application', 'degree_division',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.primary_division'
        db.add_column(u'backend_application', 'primary_division',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.post_subject'
        db.add_column(u'backend_application', 'post_subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.PostgraduateSubject'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Application.current_degree_user'
        db.delete_column(u'backend_application', 'current_degree_user')

        # Deleting field 'Application.current_year'
        db.delete_column(u'backend_application', 'current_year')

        # Deleting field 'Application.current_subjects'
        db.delete_column(u'backend_application', 'current_subjects')

        # Deleting field 'Application.institution_name'
        db.delete_column(u'backend_application', 'institution_name')


    models = {
        u'backend.application': {
            'Meta': {'object_name': 'Application'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
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