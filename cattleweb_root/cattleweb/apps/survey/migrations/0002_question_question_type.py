# Generated by Django 3.1.4 on 2020-12-31 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='check', max_length=200),
        ),
    ]
