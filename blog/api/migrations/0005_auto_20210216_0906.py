# Generated by Django 3.1.6 on 2021-02-16 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20210216_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='upvote',
            name='pressed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='api.post'),
        ),
    ]
