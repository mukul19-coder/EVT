# Generated by Django 2.0.7 on 2020-12-02 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0011_auto_20201028_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_6',
            name='aname',
        ),
        migrations.RemoveField(
            model_name='order_6',
            name='anumber',
        ),
        migrations.RemoveField(
            model_name='order_6',
            name='bname',
        ),
        migrations.RemoveField(
            model_name='order_6',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order_6',
            name='transactionid',
        ),
    ]
