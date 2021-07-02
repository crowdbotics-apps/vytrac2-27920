# Generated by Django 3.2.4 on 2021-07-02 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('description', models.TextField(max_length=200, null=True, unique=True)),
                ('threshold', models.CharField(max_length=200, null=True, unique=True)),
                ('goal', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CPTcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(blank=True, max_length=999, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=999, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=999, unique=True)),
                ('code', models.CharField(max_length=999, unique=True)),
                ('description', models.TextField(max_length=400)),
                ('score', models.PositiveIntegerField(blank=True, help_text='the score represent the danger of the disease', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiseaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=999, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('second_phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('relationship', models.CharField(blank=True, choices=[('family', 'family'), ('friend', 'friend'), ('cousin', 'cousin'), ('siblings', 'siblings'), ('parent', 'parent'), ('partner', 'partner')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('primary', models.CharField(blank=True, max_length=50)),
                ('secondary', models.CharField(blank=True, max_length=50)),
                ('subscriber', models.CharField(blank=True, max_length=50)),
                ('number', models.PositiveBigIntegerField(blank=True)),
                ('group_number', models.PositiveBigIntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('score', models.PositiveIntegerField(blank=True, help_text='the score represent the how much is the patient need attentian or in danger', null=True)),
                ('gender_identity', models.CharField(blank=True, max_length=50)),
                ('marital_status', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_adhering', models.BooleanField(default=False)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('eligible', models.BooleanField(default=False)),
                ('report_generated', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_payed', models.BooleanField(default=False)),
                ('amount', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='PrimaryCarePhysician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('office_phone', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('office_fax', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(max_length=999, unique=True)),
                ('priority', models.CharField(blank=True, choices=[('low', 'low'), ('averge', 'averge'), ('heigh', 'heigh')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RPMplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=999, unique=True)),
                ('description', models.TextField(max_length=400)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=999, unique=True)),
                ('description', models.TextField(max_length=400)),
                ('score', models.PositiveIntegerField(blank=True, help_text='the score represent the danger of the symptom', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SymptomsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('symptoms', models.ManyToManyField(to='patients.Symptom')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
