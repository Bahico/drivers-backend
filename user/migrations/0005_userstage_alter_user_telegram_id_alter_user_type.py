# Generated by Django 5.0.6 on 2024-06-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_telegram_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=200, unique=True)),
                ('step', models.CharField(max_length=200)),
                ('step_under', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Driver'), (3, 'Simple')], default=3),
        ),
    ]
