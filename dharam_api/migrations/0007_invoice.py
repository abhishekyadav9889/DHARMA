# Generated by Django 4.2 on 2023-04-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharam_api', '0006_alter_feedback_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
