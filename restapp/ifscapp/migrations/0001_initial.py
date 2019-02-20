# Generated by Django 2.1.7 on 2019-02-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IFSC', models.CharField(max_length=11)),
                ('Bank_id', models.CharField(max_length=10)),
                ('Branch', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=300)),
                ('City', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('BankName', models.CharField(max_length=100)),
            ],
        ),
    ]
