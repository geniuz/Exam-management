# Generated by Django 2.1 on 2018-08-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_auto_20180830_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='abbreviation',
            field=models.CharField(default='a', max_length=4),
            preserve_default=False,
        ),
    ]