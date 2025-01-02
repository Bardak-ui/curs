# Generated by Django 5.1.4 on 2024-12-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0015_remove_project_owner_remove_project_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Выполнено', 'Complited'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Низкий', 'Low'), ('Average', 'Cредний'), ('High', 'Высокий'), ('Не указан', 'Not specified')], default='Not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Выполнено', 'Complited'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
    ]
