# Generated by Django 4.1.3 on 2022-11-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_remove_book_dni_remove_book_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookloan',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='bookloan',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bookloan',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='historicalbookloan',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='historicalbookloan',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='historicalbookloan',
            name='last_name',
        ),
        migrations.AddField(
            model_name='bookloan',
            name='status',
            field=models.CharField(max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='historicalbookloan',
            name='status',
            field=models.CharField(max_length=50, null=True, verbose_name='Status'),
        ),
    ]
