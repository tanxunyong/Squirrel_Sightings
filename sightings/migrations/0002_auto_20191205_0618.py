# Generated by Django 2.2.7 on 2019-12-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='Unique Squirrel ID', max_length=14, primary_key=True, serialize=False),
        ),
    ]
