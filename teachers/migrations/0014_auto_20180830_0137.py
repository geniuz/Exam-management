# Generated by Django 2.1 on 2018-08-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0013_subjects_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='abbreviation',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]