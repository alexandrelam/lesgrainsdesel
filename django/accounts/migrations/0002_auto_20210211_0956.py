# Generated by Django 3.1.4 on 2021-02-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
