# Generated by Django 2.1.15 on 2021-07-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_thread_velcro'),
    ]

    operations = [
        migrations.AddField(
            model_name='elastic',
            name='stock',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='thread',
            name='stock',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='velcro',
            name='stock',
            field=models.IntegerField(default='0'),
        ),
    ]
