# Generated by Django 4.2.4 on 2023-10-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjob',
            name='requirements',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
