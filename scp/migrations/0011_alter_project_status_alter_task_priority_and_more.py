# Generated by Django 5.1.4 on 2024-12-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0010_remove_profile_image_profile_avatar_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Complited', 'Выполнено'), ('In Development', 'В разработке'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Низкий', 'Low'), ('Average', 'Cредний'), ('Высокий', 'High'), ('Not specified', 'Не указан')], default='Not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Complited', 'Выполнено'), ('In Development', 'В разработке'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
    ]
