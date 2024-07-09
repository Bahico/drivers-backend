# Generated by Django 5.0.5 on 2024-07-08 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0006_alter_user_type'),
    ]

    operations = [
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
                ('message_id', models.IntegerField()),
                ('text', models.TextField()),
                ('driver_order_index', models.IntegerField(default=0)),
                ('accept_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.driverorder')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='user.user')),
                ('drivers', models.ManyToManyField(related_name='queue_message', to='message.driverorder')),
            ],
        ),
    ]