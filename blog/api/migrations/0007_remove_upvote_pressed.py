# Generated by Django 3.1.6 on 2021-02-18 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210216_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='pressed',
        ),
    ]
