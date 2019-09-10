# Generated by Django 2.2.1 on 2019-06-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('aboutme', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'wdb_bloghome',
            },
        ),
    ]
