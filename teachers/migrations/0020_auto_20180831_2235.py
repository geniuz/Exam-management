# Generated by Django 2.1 on 2018-08-31 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0019_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
