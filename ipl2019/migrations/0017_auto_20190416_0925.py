# Generated by Django 2.1.5 on 2019-04-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl2019', '0016_auto_20190416_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
