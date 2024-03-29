# Generated by Django 3.2.12 on 2024-02-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_id', models.IntegerField()),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
    ]
