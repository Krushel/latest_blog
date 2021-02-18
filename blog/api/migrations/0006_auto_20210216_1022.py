# Generated by Django 3.1.6 on 2021-02-16 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20210216_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upvote',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='upvote',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='pressed',
            field=models.BooleanField(),
        ),
    ]
