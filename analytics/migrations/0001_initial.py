# Generated by Django 4.0.6 on 2022-07-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweetid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetid', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tweetkeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.JSONField(null=True)),
            ],
        ),
    ]
