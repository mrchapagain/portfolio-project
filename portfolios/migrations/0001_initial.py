# Generated by Django 4.0.6 on 2022-07-29 15:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('sum', models.TextField(default=' ', max_length=255)),
                ('body', ckeditor.fields.RichTextField(default=' ')),
            ],
        ),
    ]
