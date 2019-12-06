# 2018 Central Park Squirrel Census: A Sighting Tracking Visualization Webapplication

> **Group Name**: Proejct Group 76   |   **Group Member**: Xunyong Tan  Tianyan Wang | **UNIs**: [xt2227,tw2730] 

This file is written to describing the tools, the use and the behaviour of this webapplication for squirrel sighting tracking, intended for those with a pleasant or traumatic childhood squirrel experience and crystal bath experience in Sedona at the Central Park in the city of New York. 

# Content
Content

# Functions

This **Squirrel Sighting Tracking Webapplication** is based on Django development and keeps track of all the known and recorded squirrels in 2018 at the Central Park as a starting observation. In this webapplication, the squirrel tracking dataset is imported. Users can add,delect, edit and view the statistics of Squirrel Sighting data and get the visualization of the geographic information of all the squirrel sightings generalized in the map.

# Dataset

The squirrel sighting data for this webapplication can be imported from [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data), which was collected and published by the [**Squirrel Census Comminity**](https://www.thesquirrelcensus.com/) in 2019. 

This dataset contains data from 3,023 different squirrel sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans at the Central Park.

# Management Commands

> **Import**: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

    -	$ python manage.py import_squirrel_data /path/to/file.csv

> **Export**: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 

    -	$ python manage.py export_squirrel_data /path/to/file.csv

# 


# Contributors

**Group Name**: Proejct Group 76      
**Group Member**: Xunyong Tan(uni:xt2227)  Tianyan Wang(uni:tw2730) 
**UNIs**: [xt2227 , tw2730]

