# Generated by Django 5.0.5 on 2024-07-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
