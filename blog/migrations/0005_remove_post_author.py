# Generated by Django 3.1.1 on 2020-11-19 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]