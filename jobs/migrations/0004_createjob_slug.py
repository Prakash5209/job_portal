# Generated by Django 4.2.4 on 2023-08-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_createjob_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjob',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
