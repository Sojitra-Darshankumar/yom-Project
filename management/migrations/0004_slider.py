# Generated by Django 4.2 on 2023-05-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_admin1_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tital', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=10000)),
                ('Picture', models.FileField(default='', upload_to='')),
            ],
        ),
    ]