# Generated by Django 4.2 on 2023-06-07 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_comments_blogid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments',
        ),
    ]