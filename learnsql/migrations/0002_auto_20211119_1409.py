# Generated by Django 3.2.9 on 2021-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnsql', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contact_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='contact_last_name',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
