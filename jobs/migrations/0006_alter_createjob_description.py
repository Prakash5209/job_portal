# Generated by Django 4.2.4 on 2023-08-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_timestampmodel_remove_createjob_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createjob',
            name='description',
            field=models.TextField(default='this is awesome'),
        ),
    ]
