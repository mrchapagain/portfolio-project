# Generated by Django 4.0.4 on 2022-07-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetid',
            name='tweetid',
            field=models.JSONField(default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='tweetkeyword',
            name='keyword',
            field=models.JSONField(default=' ', null=True),
        ),
    ]
