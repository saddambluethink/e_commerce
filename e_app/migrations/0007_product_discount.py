# Generated by Django 3.2.9 on 2021-12-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0006_alter_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=5),
        ),
    ]
