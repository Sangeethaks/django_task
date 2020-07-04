# Generated by Django 2.2.14 on 2020-07-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=200)),
                ('tz', models.CharField(max_length=200)),
            ],
        ),
    ]
