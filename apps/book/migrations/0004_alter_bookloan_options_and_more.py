# Generated by Django 4.1.3 on 2022-11-15 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_author_name_remove_historicalauthor_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookloan',
            options={'verbose_name': 'bookloan', 'verbose_name_plural': 'bookloans'},
        ),
        migrations.AlterModelOptions(
            name='historicalbookloan',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical bookloan', 'verbose_name_plural': 'historical bookloans'},
        ),
    ]