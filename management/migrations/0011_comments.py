# Generated by Django 4.2.1 on 2023-06-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_alter_slider_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Picture', models.FileField(default='', upload_to='')),
                ('Subject', models.CharField(max_length=100)),
                ('Comment', models.TextField()),
            ],
        ),
    ]
