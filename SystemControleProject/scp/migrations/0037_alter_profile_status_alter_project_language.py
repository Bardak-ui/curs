# Generated by Django 5.1.4 on 2025-01-02 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0036_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Заблокирован', 'Banned'), ('Не заблокирован', 'Not banned')], default='Not banned', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('C', 'С'), ('C++', 'С++'), ('C#', 'С#'), ('Go', 'Go'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('Kotlin', 'Kotlin'), ('PHP', 'PHP'), ('Python', 'Python'), ('Ruby', 'Ruby'), ('Rust', 'Rust'), ('TypeScript', 'TypeScript'), ('Swift', 'Swift'), ('Shell', 'Shell'), ('Perl', 'Perl'), ('Lua', 'Lua'), ('SQL', 'SQL'), ('Assembly', 'Ассемблер'), ('Not specified', 'Не указан')], default='Not specified', max_length=50),
        ),
    ]
