# Generated by Django 5.0.2 on 2024-02-14 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_visit_visit_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='visit_time',
        ),
    ]
