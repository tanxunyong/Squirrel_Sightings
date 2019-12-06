# 2018 Central Park Squirrel Census: A Sighting Tracking Visualization Webapplication

> **Group Name**: Proejct Group 76   |   **Group Member**: Xunyong Tan  Tianyan Wang | **UNIs**: [xt2227,tw2730] 

This file is written to describing the tools, the use and the behaviour of this webapplication for squirrel sighting tracking, intended for those with a pleasant or traumatic childhood squirrel experience and crystal bath experience in Sedona at the Central Park in the city of New York. 

## Content
Content

## Functions

This **Squirrel Sighting Tracking Webapplication** is based on Django development and keeps track of all the known and recorded squirrels in 2018 at the Central Park as a starting observation. In this webapplication, the squirrel tracking dataset is imported. Users can add,delect, edit and view the statistics of Squirrel Sighting data and get the visualization of the geographic information of all the squirrel sightings generalized in the map.

## Dataset

The squirrel sighting data for this webapplication can be imported from [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data), which was collected and published by the [**Squirrel Census Comminity**](https://www.thesquirrelcensus.com/) in 2019. 

This dataset contains data from 3,023 different squirrel sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans at the Central Park.

## Installation
Clone this repository into your project with the following SSH:
```bash
git@github.com:tanxunyong/Squirrel_Sightings.git
```
## Installation of Dependencies

As many platforms as a Services expect a requirements.txt file in the root of projects, install the production requirements using this code:
``` bash
$ pip install -r requirements.txt
```

## Management Commands

To import and export the dataset, use these management commands:

> **Import**: A command that can be used to import the data from the 2018 census file in CSV format. The file path should be specified at the command line after the name of the management command.

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

> **Export**: A command that can be used to export the data from the 2018 cencus file in CSV format. The file path should be specified at the command line after the name of the management command. 

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```

## API
Run the server and then go to the brower to open the development server, adding different views location to the url will lead to different API with different function.

> **Map**:  
* Behavior: Map is a view that shows a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).
* Located at: /map
* Warning: If you plot 100 notes at once, the browser may freeze for a while.
 
> **Sightings**: 
* Behavior: Sightings is a view that lists all squirrel sightings with links to edit and add sightings.
* Located at: /sightings
 
> **Update**: 
* Behavior: Update is a view to update a particular sighting. Add a specific unique squirrel id in the location to check and update the individual information of a squirrel.
* Located at: /sightings/<unique-squirrel-id>
 
> **Add**: 
* Behavior: Add is a view to create a new sighting to the database. Open the link and input the necessary information: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent and Runs from. After adding the squirrel, it will be added to the sighting list and be updated.
* Located at: /sightings/add
 
> **Delete**: 
* Behavior: Delete is a view to update a particular sighting. Add a specific unique squirrel id in the location to view and delete individual information of a squirrel.
* Located at: /sightings/<unique-squirrel-id>
 
> **General**: 
* Behavior: General Stats is a view to view important general information about the squirrel sightings. In this page, typical attritbutes of all the squirrel sightings are listed.
* Located at: /sightings/stats

## Detaild Background

Eccentric billionaire Joffrey Hosencratz just purchased the web development company we work for. We’ve met him once in an elevator and he relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. Therefore we are asked to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 

## Issue Tracker and Mailing List
Bug reports are welcome!  You can submit pull requests on 
GitHub <git@github.com:tanxunyong/Squirrel_Sightings.git>.

## Contributors

**Group Name**: Proejct Group 76      
**Group Member**: Xunyong Tan(uni:xt2227)  Tianyan Wang(uni:tw2730) 
**UNIs**: [xt2227 , tw2730]

