# Generated by Django 3.0.5 on 2020-10-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201004_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.TextField(choices=[('new', 'new'), ('planned', 'planned'), ('performing', 'performing'), ('completed', 'completed')], default='new'),
        ),
    ]