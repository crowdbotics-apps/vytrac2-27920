# Generated by Django 3.2.4 on 2021-07-03 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('resolution', models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='deadline')),
                ('state', models.CharField(choices=[('to-do', 'To Do'), ('in_progress', 'In Progress'), ('blocked', 'Blocked'), ('done', 'Done'), ('dismissed', 'Dismissed')], default='to-do', max_length=20, verbose_name='state')),
                ('priority', models.CharField(choices=[('00_low', 'Low'), ('10_normal', 'Normal'), ('20_high', 'High'), ('30_critical', 'Critical'), ('40_blocker', 'Blocker')], default='10_normal', max_length=20, verbose_name='priority')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('type', models.CharField(choices=[('daily_plan', 'Daily plan'), ('task', 'task'), ('emergency', 'Emergency')], default='10_normal', max_length=20, verbose_name='type')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('dates', models.ManyToManyField(blank=True, related_name='responsible', to='calendars.Event')),
                ('pations', models.ManyToManyField(blank=True, related_name='pations_daily_plan', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ManyToManyField(blank=True, related_name='responsible', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL, verbose_name='assigned to')),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
    ]
