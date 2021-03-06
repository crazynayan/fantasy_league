# Generated by Django 2.1.5 on 2019-04-16 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipl2019', '0015_auto_20190412_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipl2019.Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipl2019.Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(related_name='matches', through='ipl2019.TeamMatch', to='ipl2019.Team'),
        ),
    ]
