# Generated by Django 2.2 on 2019-05-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('profession', models.CharField(blank=True, choices=[('doctor', 'doctor'), ('singer', 'singer')], default='', max_length=20)),
                ('language', models.CharField(blank=True, choices=[('english', 'english'), ('punjabi', 'punjabi')], max_length=20)),
                ('pro', models.BooleanField(default=False)),
            ],
        ),
    ]
