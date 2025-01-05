# Generated by Django 5.1.4 on 2025-01-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0043_profile_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.CharField(choices=[('Онлайн', 'Online'), ('Офлайн', 'Оffline'), ('Деактивирована', 'Deactivated')], default='Offline', max_length=50),
        ),
    ]
