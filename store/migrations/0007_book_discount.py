# Generated by Django 5.0.6 on 2024-07-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_userbookrelation_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount',
            field=models.IntegerField(max_length=4, null=True),
        ),
    ]