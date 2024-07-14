# Generated by Django 5.0.6 on 2024-06-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_book_readers_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Ok'), (4, 'Fine'), (5, 'Well')], null=True),
        ),
    ]