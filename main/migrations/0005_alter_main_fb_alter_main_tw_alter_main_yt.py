# Generated by Django 4.0.2 on 2022-03-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_fb_main_tw_main_yt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.TextField(),
        ),
    ]