# Generated by Django 4.2.2 on 2023-06-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Country Name')),
                ('capital', models.CharField(max_length=100, verbose_name='Capital City')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateField(blank=True, null=True, verbose_name='Updated Date')),
            ],
        ),
    ]