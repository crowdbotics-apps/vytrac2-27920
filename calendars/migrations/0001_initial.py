# Generated by Django 3.2.4 on 2021-07-02 08:18

import Functions.MyViews
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=999)),
                ('description', models.CharField(blank=True, max_length=999, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=999, null=True)),
                ('description', models.TextField(blank=True, max_length=9999, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('from_time', models.TimeField(blank=True, null=True)),
                ('to_time', models.TimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('recurrence', Functions.MyViews.Rec(blank=True, choices=[('0 month', 'Every month.'), ('0 3 month', 'Every 3 months.'), ('0 6 month', 'Every 6 months.'), ('0 year', 'Every year.'), ('1 sunday', 'Every sunday.'), ('1 monday', 'Every monday.'), ('1 tuesday', 'Every tuesday.'), ('1 wednesday', 'Every wednesday.'), ('1 thursday', 'Every thursday.'), ('1 friday', 'Every friday.'), ('1 saturday', 'Every saturday.'), ('2 january ', 'Every january.'), ('2 february', 'Every february.'), ('2  march', 'Every march.')], max_length=93, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('priority', models.CharField(blank=True, choices=[('low', 'low'), ('averge', 'averge'), ('heigh', 'heigh')], max_length=50)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
    ]
