# Generated by Django 4.0.2 on 2022-03-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catname', models.CharField(max_length=50)),
                ('catid', models.IntegerField()),
            ],
        ),
    ]
