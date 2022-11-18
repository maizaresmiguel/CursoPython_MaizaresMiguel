# Generated by Django 4.1.3 on 2022-11-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_options_alter_historicalbook_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='historicalauthor',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='historicalauthor',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='historicalauthor',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='last_name'),
        ),
    ]
