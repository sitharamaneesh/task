# Generated by Django 3.2.5 on 2021-09-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
