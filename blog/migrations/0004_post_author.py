# Generated by Django 3.1.1 on 2020-11-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=123, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]