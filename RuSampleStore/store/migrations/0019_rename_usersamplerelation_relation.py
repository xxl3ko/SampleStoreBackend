# Generated by Django 4.1.6 on 2023-03-23 17:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0018_alter_sample_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSampleRelation',
            new_name='Relation',
        ),
    ]
