# Generated by Django 4.1.3 on 2022-11-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_bookloan_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='book',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='historicalbook',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='historicalbook',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='historicalbook',
            name='last_name',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=50, verbose_name='isbn'),
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='historicalbook',
            name='isbn',
            field=models.CharField(blank=True, max_length=50, verbose_name='isbn'),
        ),
        migrations.AddField(
            model_name='historicalbook',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
    ]
