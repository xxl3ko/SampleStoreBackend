# Generated by Django 4.1.6 on 2023-04-05 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_sample_file_src'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='title',
            new_name='name',
        ),
    ]