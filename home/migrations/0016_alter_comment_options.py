# Generated by Django 3.2 on 2021-04-29 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_body_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added']},
        ),
    ]