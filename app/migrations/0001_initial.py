# Generated by Django 4.1.6 on 2023-02-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBSStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200, unique=True)),
                ('rank', models.IntegerField()),
                ('link', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('snippet', models.CharField(max_length=200)),
                ('html', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]