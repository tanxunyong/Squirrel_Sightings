# 2018 Central Park Squirrel Census: A Sighting Tracking and Visualization Webapplication

> **Group Name**: Project Group 76   |   **Group Member**: Xunyong Tan ,  Tianyan Wang | **UNIs**: [xt2227,tw2730] 

This file is written to describe the tools, the use and the behaviour of this webapplication for squirrel sighting tracking, intended to give users full control over their interactions with squirrels in Central Park, New York City. 

## Content
- [Functions](#heading)
- [Dataset](#heading-2)
- [Installation](#heading-3)
- [Installation of Dependencies](#heading-4)
- [Management Commands](#heading-5)
- [API](#heading-6)
- [Deployment](#heading-7)
- [Detailed Background](#heading-8)
- [Issue Tracker and Mailing List](#heading-9)
- [Contributors](#heading-10)


<a name="heading"></a>
## Functions

This **Squirrel Sighting Tracking Webapplication** is based on Django development and keeps track of all the known and recorded squirrels in 2018 at the Central Park. In this webapplication, the squirrel tracking dataset is imported. Users can add, delete, edit and view the statistics of Squirrel Sighting data and get the view of all the squirrel sightings on a map. To explore more about the functions in deployed web, you can open [**Squirrel Sightings**](https://green-webbing-255500.appspot.com) and follow the guide.

<a name="heading-2"></a>
## Dataset

The squirrel sighting data for this webapplication can be imported from [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data), which was collected and published by the [**Squirrel Census Community**](https://www.thesquirrelcensus.com/) in 2019. 

This dataset contains data from 3,023 different squirrel sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans at the Central Park.

<a name="heading-3"></a>
## Installation
Clone this repository into your project with the following SSH:
```bash
git@github.com:tanxunyong/Squirrel_Sightings.git
```

<a name="heading-4"></a>
## Installation of Dependencies

As many platforms and Services expect a requirements.txt file in the root of projects, install the production requirements using this code:
``` bash
$ pip install -r requirements.txt
```
<a name="heading-5"></a>
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
<a name="heading-6"></a>
## API
Run the server and then go to the brower to open the development server, adding different views location to the url will lead to different API with different function.

> **Map**:  
* **Behavior**: Map is a view that shows a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).
* **Located at**: /map
* **Warning**: If you plot 100 sightings at once, the browser may freeze for a while.
 
> **Sightings**: 
* **Behavior**: Sightings is a view that lists all squirrel sightings with links to edit and add sightings.
* **Located at**: /sightings
 
> **Update**: 
* **Behavior**: Update is a view to update a particular sighting. Add a specific unique squirrel id in the location to check and update the individual information of a squirrel.
* **Located at**: /sightings/<unique-squirrel-id>
 
> **Add**: 
* **Behavior**: Add is a view to create a new sighting to the database. Open the link and input the necessary information: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent and Runs from. After adding the squirrel, it will be added to the sighting list and be updated.
* **Located at**: /sightings/add
 
> **Delete**: 
* **Behavior**: Delete is a view to update a particular sighting. Add a specific unique squirrel id in the location to view and delete individual information of a squirrel.
* **Located at**: /sightings/<unique-squirrel-id>
 
> **General**: 
* **Behavior**: General Stats is a view to view important general information about the squirrel sightings. In this page, typical attributes of all the squirrel sightings are listed.
* **Located at**: /sightings/stats

<a name="heading-7"></a>
## Deployment
To explore the deployed webapplication, open the following link and click the link shown in the guide page.(https://green-webbing-255500.appspot.com)
https://green-webbing-255500.appspo

<a name="heading-8"></a>
## Detaild Background
<div align="center">
  <img src="https://media.npr.org/assets/img/2017/04/25/istock-115796521-fcf434f36d3d0865301cdcb9c996cfd80578ca99-s1600-c85.jpg",height="500" width="480" >
</div>
Eccentric billionaire Joffrey Hosencratz just purchased the web development company we work for. We’ve met him once in an elevator and he relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show [**Rick and Morty**](https://www.youtube.com/watch?v=C5SU_K-GFKk/) and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. Therefore we are asked to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 

<a name="heading-9"></a>
## Issue Tracker and Mailing List
Bug reports are welcome!  You can submit pull requests on GitHub <git@github.com:tanxunyong/Squirrel_Sightings.git> if you spot any issues when executing our code.

<a name="heading-10"></a>
## Contributors

**Group Name**: Project Group 76      

**Group Member**: Xunyong Tan(uni: xt2227),  Tianyan Wang(uni: tw2730) 

**UNIs**: [xt2227 , tw2730]

