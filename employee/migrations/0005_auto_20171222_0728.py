# Generated by Django 2.0 on 2017-12-21 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20171222_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='club',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]
