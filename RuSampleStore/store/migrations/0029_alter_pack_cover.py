# Generated by Django 4.1.6 on 2023-04-06 06:06

import base.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_rename_cover_src_pack_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='cover',
            field=models.ImageField(null=True, upload_to=base.services.get_path_upload_cover),
        ),
    ]
