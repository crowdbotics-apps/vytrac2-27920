# Generated by Django 3.2.4 on 2021-07-02 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.SlugField()),
                ('if_item', models.CharField(blank=True, choices=[('user.change_username', 'user | change username')], max_length=50)),
                ('if_ction', models.CharField(blank=True, choices=[('user.change_username', 'user | change username')], max_length=50)),
                ('then_action', models.CharField(blank=True, choices=[('user.change_username', 'user | change username')], max_length=50)),
                ('then_set_value', models.CharField(blank=True, choices=[('user.change_username', 'user | change username')], max_length=50)),
                ('then_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
