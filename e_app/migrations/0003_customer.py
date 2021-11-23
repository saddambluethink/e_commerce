# Generated by Django 3.2.9 on 2021-11-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0002_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=10)),
            ],
        ),
    ]
