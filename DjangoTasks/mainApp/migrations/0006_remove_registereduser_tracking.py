# Generated by Django 3.2.4 on 2021-06-16 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_registereduser_post_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='tracking',
        ),
    ]
