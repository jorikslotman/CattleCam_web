# Generated by Django 3.1.4 on 2021-01-13 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_type', models.CharField(choices=[('radio', 'Radio button'), ('checkbox', 'Checkbox'), ('input', 'Input'), ('textarea', 'Text field')], default='checkbox', max_length=200)),
                ('public_description', models.CharField(max_length=200)),
                ('private_description', models.CharField(max_length=200, null=True)),
                ('order_num', models.IntegerField(default=1)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('public_title', models.CharField(default='Vragenlijst', max_length=200)),
                ('public_description', models.TextField(default='Met deze vragenlijst willen we graag ... ', null=True)),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('private_title', models.CharField(default='marktonderzoek', max_length=200)),
                ('private_description', models.TextField(default='Is CattleCam de kip met gouden eieren?', null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=400)),
                ('response_time', models.DateTimeField(auto_now_add=True)),
                ('submitted', models.BooleanField(default=False)),
                ('submitted_id', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('private_description', models.TextField(null=True)),
                ('order_num', models.IntegerField(default=1)),
                ('published', models.BooleanField(default=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question'),
        ),
    ]
