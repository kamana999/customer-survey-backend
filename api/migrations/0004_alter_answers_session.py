# Generated by Django 3.2.7 on 2021-09-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210911_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='session',
            field=models.CharField(max_length=500),
        ),
    ]