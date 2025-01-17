# Generated by Django 5.1.4 on 2025-01-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0005_remove_project_files_project_complexity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('C', 'С'), ('C++', 'С++'), ('C#', 'С#'), ('Go', 'Go'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('Kotlin', 'Kotlin'), ('PHP', 'PHP'), ('Python', 'Python'), ('Ruby', 'Ruby'), ('Rust', 'Rust'), ('TypeScript', 'TypeScript'), ('Swift', 'Swift'), ('Shell', 'Shell'), ('Perl', 'Perl'), ('Lua', 'Lua'), ('SQL', 'SQL'), ('Assembly', 'Ассемблер'), ('Не указан', 'Не указан')], default='Не указан', max_length=50, verbose_name='Язык программирования'),
        ),
    ]
