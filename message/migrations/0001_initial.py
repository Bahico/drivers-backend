# Generated by Django 5.1.2 on 2024-10-13 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255)),
                ('client_message_id', models.IntegerField()),
                ('message_id', models.IntegerField()),
                ('voice', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DriverOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('driver_order_index', models.IntegerField(default=0)),
                ('accept_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.driverorder')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='user.user')),
                ('drivers', models.ManyToManyField(default=[], related_name='queue_message', to='message.driverorder')),
            ],
        ),
    ]
