# Generated by Django 2.2.1 on 2019-05-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='user',
            field=models.CharField(default='NULL', max_length=12),
        ),
    ]
