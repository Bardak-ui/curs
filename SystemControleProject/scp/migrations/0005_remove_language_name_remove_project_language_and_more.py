# Generated by Django 5.1.4 on 2024-12-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scp', '0004_language_name_alter_project_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='language',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Выполнено', 'Complited'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Низкий'), ('Cредний', 'Average'), ('Высокий', 'High'), ('Not specified', 'Не указан')], default='Not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Выполнено', 'Complited'), ('В разработке', 'In Development'), ('Waiting', 'Ожидает')], default='Waiting', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('C', 'Си'), ('C++', 'Си плюс плюс'), ('C#', 'Си шарп'), ('Go', 'Го'), ('Java', 'Джава'), ('JavaScript', 'Джаваскрипт'), ('Kotlin', 'Котлин'), ('PHP', 'ПХП'), ('Python', 'Пайтон'), ('Ruby', 'Руби'), ('Rust', 'Раст'), ('Scala', 'Скала'), ('TypeScript', 'Тайпскрипт'), ('Swift', 'Свифт'), ('R', 'Эр'), ('Dart', 'Дарт'), ('Shell', 'Шелл'), ('Haskell', 'Хаскелл'), ('Perl', 'Перл'), ('Lua', 'Луа'), ('Elixir', 'Эликсир'), ('Erlang', 'Эрланг'), ('Visual Basic', 'Вижуал Бейсик'), ('Objective-C', 'Обжектив-Си'), ('Fortran', 'Фортран'), ('COBOL', 'Кобол'), ('F#', 'Эф шарп'), ('SQL', 'Эс-Кью-Эл'), ('Julia', 'Джулия'), ('Racket', 'Ракет'), ('Tcl', 'Тикл'), ('VHDL', 'Ви-Эйч-Ди-Эл'), ('Verilog', 'Верилог'), ('Assembly', 'Ассемблер'), ('Prolog', 'Пролог'), ('Ada', 'Ада'), ('Matlab', 'Матлаб'), ('Crystal', 'Кристал'), ('D', 'Ди'), ('Groovy', 'Груви'), ('Nim', 'Ним'), ('Solidity', 'Солидити'), ('COQ', 'Кок'), ('APL', 'Эй-Пи-Эль'), ('Ballerina', 'Баллерина'), ('Not specified', 'Не указан')], default='Not specified', max_length=50),
        ),
    ]
