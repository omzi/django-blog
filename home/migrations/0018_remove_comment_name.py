# Generated by Django 3.2 on 2021-04-29 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]