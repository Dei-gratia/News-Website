# Generated by Django 4.0.2 on 2022-03-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.TextField(default=''),
        ),
    ]