# Generated by Django 4.1.7 on 2023-03-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotable',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
