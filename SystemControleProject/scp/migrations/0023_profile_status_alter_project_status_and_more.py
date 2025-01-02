# Generated by Django 5.1.4 on 2024-12-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0022_alter_project_status_alter_task_assignee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Baned', 'Заблокирован'), ('Не заблокирован', 'Not baned')], default='Not baned', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Complited', 'Выполнено'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Низкий', 'Low'), ('Average', 'Cредний'), ('Высокий', 'High'), ('Not specified', 'Не указан')], default='Not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Complited', 'Выполнено'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
    ]
