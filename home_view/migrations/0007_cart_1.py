# Generated by Django 2.0.7 on 2020-10-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0006_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pId', models.CharField(max_length=100)),
                ('qty', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('uId', models.CharField(max_length=100)),
                ('uo', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
