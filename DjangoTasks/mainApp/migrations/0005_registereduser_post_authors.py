# Generated by Django 3.2.4 on 2021-06-16 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20210616_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='post_authors',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mainApp.feeditem'),
            preserve_default=False,
        ),
    ]
