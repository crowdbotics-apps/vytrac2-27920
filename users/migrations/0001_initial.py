# Generated by Django 3.2.4 on 2021-07-02 08:18

import Functions.MyViews
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_archived', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'only letter from a-z are allowed')])),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('secon_email', models.EmailField(blank=True, max_length=250)),
                ('first_name', models.CharField(blank=True, max_length=999, null=True)),
                ('last_name', models.CharField(blank=True, max_length=999, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=999, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_role_verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('receive_newsletter', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=999, null=True)),
                ('about_me', models.TextField(blank=True, max_length=500, null=True)),
                ('phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('second_phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('imageUrl', models.CharField(blank=True, max_length=900, null=True)),
                ('age', models.CharField(blank=True, max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'get_latest_by': 'date_created',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('watch', models.CharField(blank=True, choices=[('patien profiel', 'patien profiel')], max_length=50)),
                ('settings_type', models.CharField(choices=[('notifcations', 'notifcations settings'), ('reporet', 'reporet tashbord settings')], max_length=999, unique=True)),
                ('see_all', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('alert_date', models.DateTimeField(blank=True, help_text='specify time to remind you about this note', null=True)),
                ('user', models.ManyToManyField(blank=True, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Availablity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=999, null=True)),
                ('description', models.TextField(blank=True, max_length=9999, null=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('recurrence', Functions.MyViews.Rec(blank=True, choices=[('0 month', 'Every month.'), ('0 3 month', 'Every 3 months.'), ('0 6 month', 'Every 6 months.'), ('0 year', 'Every year.'), ('1 sunday', 'Every sunday.'), ('1 monday', 'Every monday.'), ('1 tuesday', 'Every tuesday.'), ('1 wednesday', 'Every wednesday.'), ('1 thursday', 'Every thursday.'), ('1 friday', 'Every friday.'), ('1 saturday', 'Every saturday.'), ('2 january ', 'Every january.'), ('2 february', 'Every february.'), ('2  march', 'Every march.')], max_length=93)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availablity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('home', models.CharField(max_length=999, unique=True)),
                ('apt', models.CharField(max_length=999, unique=True)),
                ('state', models.CharField(max_length=999, unique=True)),
                ('zip_code', models.CharField(max_length=999, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='settings',
            field=models.ManyToManyField(blank=True, related_name='who_can_see_comment', to='users.Settings'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.ManyToManyField(blank=True, related_name='user_sex', to='users.Sex'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
