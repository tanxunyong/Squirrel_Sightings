from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    X = models.DecimalField(
        help_text=_('longitude'),
        max_digits=16,
        decimal_places=13,
        null=True,
    )
    
    Y = models.DecimalField(
        help_text=_('latitude'),
        max_digits=16,
        decimal_places=13,
        null=True,
    )

    Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=3,
        null=True,
    )

    Hectare = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length = 3,
        null=True,
    )

    AM = 'AM'
    PM = 'PM'

    Shift = models.CharField(
        help_text=_('Morning or Afternoon Shift'),
        choices = (
            (AM, 'Before Noon'),
            (PM, 'After Noon'),
        ),
        default = AM,
        max_length =2,
        null=True,
    )

    Date = models.DateField(
        help_text=_('Date of Sighting'),
        null=True,
    )

    Hectare_Squirrel_Number = models.PositiveIntegerField(
        help_text=_('Hectare Squirrel Number'),
        null=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    BLANK = ''

    Age = models.CharField(
        help_text=_('Squirrel Age'),
        choices = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (UNKNOWN, '?'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length=10,
        null=True,
    )

    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMMON = 'Cinnammon'
    BLANK = ''

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary Fur Color'),
        choices = (
            (GRAY, 'Gray'),
            (BLACK, 'Black'),
            (CINNAMMON, 'Cinnammon'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length = 10,
        null=True,
    )

    G = 'Gray'
    B = 'Black'
    C = 'Cinnammon'
    W = 'White'
    BC = 'Black, Cinnammon'
    BW = 'Black, White'
    BCW = 'Black, Cinnammon, White'
    CW = 'Cinnammon, White'
    GB = 'Gray, Black'
    BW = 'Black, White'
    GW = 'Gray, White'
    BLANK = ''

    Highlight_Fur_Color = models.CharField(
        help_text=_('Highlight Fur Color'),
        choices = (
            (G, 'Gray'),
            (B, 'Black'),
            (C, 'Cinnammon'),
            (W, 'White'),
            (BC, 'Black, Cinnammon'),
            (BW, 'Black, White'),
            (BCW, 'Black, Cinnammon, White'),
            (CW, 'Cinammon, White'),
            (GB, 'Gray, Black'),
            (BW, 'Black, White'),
            (GW, 'Gray, White'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length = 30,
        null=True,
    )

    Combination_Fur = models.CharField(
        help_text=_('Combination of Primary and Highlight Color'),
        max_length = 100,
        null=True,
    )

    Color_Notes = models.CharField(
        help_text=_('Color Notes'),
        max_length=100,
        null=True,
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'
    BLANK = ''

    Location = models.CharField(
        help_text=_('Location'),
        choices = (
            (AG, 'Above Ground'),
            (GP, 'Ground Plane'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length=20,
        null=True
    )

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    Above_Ground_Sighter_Measurement = models.CharField(
        help_text=_('Above Ground Sighter Measurement'),
        default=FALSE,
        max_length = 10,
        null=True,
    )

    Specific_Location = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
        null=True,
    )

    Running = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Chasing = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Climbing = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Eating = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Foraging = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)

    Other_Activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
        null=True,
    )

    Kuks = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Quaas = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Moans = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Tail_Flags = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Tail_Twitches = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Approaches = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Indifferent = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Runs_From = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    
    Other_Interactions = models.CharField(
        help_text=_('Other Interactions'),
        max_length=100,
        null=True,
    )
# Create your models here.
