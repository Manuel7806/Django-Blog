# Generated by Django 4.1.5 on 2023-02-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='<django.db.models.fields.CharField>'),
        ),
    ]
