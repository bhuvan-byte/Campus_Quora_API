# Generated by Django 3.2 on 2021-05-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210509_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(blank=True, to='categories.Comment'),
        ),
    ]
