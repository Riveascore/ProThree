# Generated by Django 3.0.3 on 2020-08-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=26)),
                ('lastname', models.CharField(max_length=26)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
    ]
