# Generated by Django 3.1.1 on 2020-09-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default='put a part of your contente here'),
        ),
    ]