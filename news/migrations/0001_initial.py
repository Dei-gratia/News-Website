# Generated by Django 4.0.2 on 2022-03-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('pic', models.TextField()),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
    ]
