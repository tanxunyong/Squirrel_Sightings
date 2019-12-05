from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('X', models.FloatField(help_text='X', null=True)),
                ('Y', models.FloatField(help_text='Y', null=True)),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique Squirrel ID', max_length=13, primary_key=True, serialize=False)),
                ('Hectare', models.CharField(help_text='Hectare', max_length=3, null=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift', max_length=2, null=True)),
                ('Date', models.DateField(help_text='Date', null=True)),
                ('Hectare_Squirrel_Number', models.CharField(help_text='Hectare Squirrel Number', max_length=10, null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Unknown', '?'), ('', '')], default='', help_text='Age', max_length=10, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('', '')], default='', help_text='Primary Fur Color', max_length=10, null=True)),
                ('Highlight_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('White', 'White'), ('Black, Cinnammon', 'Black, Cinnammon'), ('Black, White', 'Black, White'), ('Black, Cinnammon, White', 'Black, Cinnammon, White'), ('Cinnammon, White', 'Cinammon, White'), ('Gray, Black', 'Gray, Black'), ('Black, White', 'Black, White'), ('Gray, White', 'Gray, White'), ('', '')], default='', help_text='Highlight Fur Color', max_length=30, null=True)),
                ('Combination_Fur', models.CharField(default='+', help_text='Combination of Primary and Highlight Color', max_length=100, null=True)),
                ('Color_Notes', models.CharField(blank=True, help_text='Color Notes', max_length=100, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('', '')], default='', help_text='Location', max_length=20, null=True)),
                ('Above_Ground_Sighter_Measurement', models.CharField(blank=True, help_text='Above Ground Sighter Measurement', max_length=10, null=True)),
                ('Specific_Location', models.CharField(blank=True, help_text='Specific Location', max_length=100, null=True)),
                ('Running', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Running', max_length=5, null=True)),
                ('Chasing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Chasing', max_length=5, null=True)),
                ('Climbing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Climbing', max_length=5, null=True)),
                ('Eating', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Eating', max_length=5, null=True)),
                ('Foraging', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Foraging', max_length=5, null=True)),
                ('Other_Activities', models.CharField(blank=True, help_text='Other Activities', max_length=100, null=True)),
                ('Kuks', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Kuks', max_length=5, null=True)),
                ('Quaas', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Quaas', max_length=5, null=True)),
                ('Moans', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Moans', max_length=5, null=True)),
                ('Tail_Flags', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Tail flags', max_length=5, null=True)),
                ('Tail_Twitches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Tail twitches', max_length=5, null=True)),
                ('Approaches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Approaches', max_length=5, null=True)),
                ('Indifferent', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Indifferent', max_length=5, null=True)),
                ('Runs_From', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Runs from', max_length=5, null=True)),
                ('Other_Interactions', models.CharField(blank=True, help_text='Other Interactions', max_length=100, null=True)),
                ('Lat_Long', models.CharField(help_text='Lat/Long', max_length=50, null=True)),
                ('Zip_Codes', models.CharField(blank=True, help_text='Zip Codes', max_length=5, null=True)),
                ('Community_Districts', models.CharField(default='19', help_text='Community Districts', max_length=5, null=True)),
                ('Borough_Boundaries', models.CharField(default='4', help_text='Borough Boundaries', max_length=5, null=True)),
                ('City_Council_Districts', models.CharField(default='19', help_text='City Council Districts', max_length=5, null=True)),
                ('Police_Precincts', models.CharField(default='13', help_text='Police Precincts', max_length=5, null=True)),
            ],
        ),
    ]
