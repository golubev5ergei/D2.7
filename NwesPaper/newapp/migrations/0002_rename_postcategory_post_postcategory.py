# Generated by Django 4.1.7 on 2023-03-06 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='PostCategory',
            new_name='postCategory',
        ),
    ]
