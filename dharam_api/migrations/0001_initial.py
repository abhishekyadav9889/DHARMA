# Generated by Django 4.2 on 2023-04-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('select_id', models.IntegerField()),
                ('id_number', models.CharField(max_length=255)),
            ],
        ),
    ]
