# Generated by Django 5.0 on 2023-12-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_accountrequest_remove_user_plan_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField()),
                ('otp', models.IntegerField()),
            ],
        ),
    ]
