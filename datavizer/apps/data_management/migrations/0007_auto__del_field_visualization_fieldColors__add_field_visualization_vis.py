# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Visualization.fieldColors'
        db.delete_column(u'data_management_visualization', 'fieldColors')

        # Adding field 'Visualization.visualizationType'
        db.add_column(u'data_management_visualization', 'visualizationType',
                      self.gf('django.db.models.fields.CharField')(default='line', max_length=255),
                      keep_default=False)

        # Adding field 'Visualization.legends'
        db.add_column(u'data_management_visualization', 'legends',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Removing M2M table for field visualizations on 'Visualization'
        db.delete_table('data_management_visualization_visualizations')

        # Adding M2M table for field datasets on 'Visualization'
        db.create_table(u'data_management_visualization_datasets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visualization', models.ForeignKey(orm[u'data_management.visualization'], null=False)),
            ('dataset', models.ForeignKey(orm[u'data_management.dataset'], null=False))
        ))
        db.create_unique(u'data_management_visualization_datasets', ['visualization_id', 'dataset_id'])


    def backwards(self, orm):
        # Adding field 'Visualization.fieldColors'
        db.add_column(u'data_management_visualization', 'fieldColors',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Deleting field 'Visualization.visualizationType'
        db.delete_column(u'data_management_visualization', 'visualizationType')

        # Deleting field 'Visualization.legends'
        db.delete_column(u'data_management_visualization', 'legends')

        # Adding M2M table for field visualizations on 'Visualization'
        db.create_table(u'data_management_visualization_visualizations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visualization', models.ForeignKey(orm[u'data_management.visualization'], null=False)),
            ('dataset', models.ForeignKey(orm[u'data_management.dataset'], null=False))
        ))
        db.create_unique(u'data_management_visualization_visualizations', ['visualization_id', 'dataset_id'])

        # Removing M2M table for field datasets on 'Visualization'
        db.delete_table('data_management_visualization_datasets')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'data_management.dataset': {
            'Meta': {'unique_together': "(('name', 'owner'),)", 'object_name': 'DataSet'},
            'datatype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_management.DataType']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'data_management.datatype': {
            'Meta': {'unique_together': "(('name', 'owner'),)", 'object_name': 'DataType'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'schema': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'data_management.datum': {
            'Meta': {'object_name': 'Datum'},
            'data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_management.DataSet']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'data_management.visualization': {
            'Meta': {'object_name': 'Visualization'},
            'datasets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['data_management.DataSet']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isPublic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legends': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'visualizationType': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['data_management']