# Generated by Django 4.2.4 on 2023-08-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_timestampmodel_remove_createjob_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjob',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
