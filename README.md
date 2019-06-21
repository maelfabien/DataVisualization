# Information Visualization

<img alt="GitHub followers" src="https://img.shields.io/github/followers/maelfabien.svg?style=social"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/maelfabien/DataVisualization.svg"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/maelfabien/DataVisualization.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/3.svg">

*Contributors : Anatoli de Bradké, Raphael Lederman, Alexandre Bec, Anthony Houdaille, Maël Fabien*

<img src="/Images/demo.gif" width="100%" height="100%">

## I. Project description

In this data visualization project, we are analyzing the road traffic accidents from the [French Database](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/)

There are 4 types of files :
- `caracteristiques` which describes the caracteristics of the accidents (location, date ...)
- `vehicules` which describes the vehicles damaged during the accident (for each vehicle individually)
- `lieux` which describes the place in which the accident took place (type of road, width...)
- `usagers` which describes the passengers or pedestrians that were hurt, the acitivity they were doing before the accident...

The are 9 attributes in the vehicles dataset (vehicle category, type of obstacle hurt...), 12 attributes for the passenger / user dataset (including age, sex, activity at the time of the accident...), 18 attributes for the location of the accident (road type, luminosity, road width...), and 16 attributes for the characteristics of the accident (date, time, GPS coordinates...). The 56 files represent 254 Mo overall.

There are a little more than 1 500 000 entries in the vehicle dataset, each entry being a single vehicle implied in an accident, 2’000’000 entries for the users dataset, each entry being a single person implied in an accident, and 900’000 entries for the location and characteristics, in which each entry represents a single accident.

We used the following technologies for this project :

![image](/Images/techno.png)

We developped a WebApp accessible right here : https://infoviz.onrender.com/

![image](/Images/webapp.png)


## II. Exploration

To allow the user to explore the data and understand the context, there are several visualizations that we present in this section : https://infoviz.onrender.com/?all=The+Data

- Age of the victime and Number of accidents per day in France :

![image](/Images/ts_2.png)

- Time of the accidents and Location of the accidents :

![image](/Images/loc_2.png)


## III. Designs

> The aim of this DataVisualization project is to identify several designs that could potentially bring value to users trying to achieve a specific task.

Our analysis could bring value to several road authorities in France :
- Communes, that are in charge of communal roads
- Departments, that are in charge of departmental roads
- The state, in charge of the national roads
- Private companies (e.g. Vinci) in charge of french highways

We except our end users to use our tool to :
- **Sensitize** the youngsters and road criminals on the danger of the roads depending on the transportation mode they are using.
- **Prevent** road dangers through a tool that would advise the best road characteristics for a road rehabilitation, and visually illustrate the outcome of the algorithm
- **Monitor** the dangers of the roads (at difference scales, including Communes, Departments and Nation) by allowing the user to select geographic zones and filters (weather conditions, hour of the day…) to gain additional insights

For this reason, we subdivided our website into several tabs (Data exploration, All roads, Communal, Departmental, National, and highway roads) and in each tab, in several sections : Sensitize, Prevent and Monitor.

### 1. Sensitization

*Motivation* :

Local police and communes are working together on sensitization of the youngster on the road dangers. One might believe that dangers for these kids arise once they have their first motorcycle or car. However, if they are involved in an accident, death rates among bike riders and pedestrians are incredibly high compared to other transportation means.

In this visualization, we created a Sankey diagram (flow chart) that shows the proportion of pedestrians, bike riders, motorcycles and cars involved in a crash these last 13 years, distinguishes if they were wearing all security equipments, and finally shows the survival rate among each category. This graph clearly illustrates the fragility and the exposure of pedestrians and bike riders, and contributes to sensitization of these populations.

*Design sketch* :

Our initial sketch of the design looked like this :

![image](/Images/sankey_final.png)

We intended to support a filter on the type of roads (communal, departmental, national), and to observe the difference of survival rate of the different categories of road users depending on the speed on the road. This would illustrate how the speed of a car impacts the survival rate of the other road users.

The design helps the reader understand the distribution of the volume of road users accident, depending on the kind of road being used, as well as the effect of speed.

*Data processing and challenges* :

One of the challenges is that each database (vehicle, passengers/pedestrians, location, characteristic) does not share a common key to join them. Indeed, the vehicle database distinguishes every vehicle implied in a same crash, whereas the characteristics of an accident only reports one observation for this specific case. On the other hand, the pedestrians and bike riders only appear in the passenger database. Overall, some data processing was needed in order to build a complete table.

Then, one of the other challenges was to find the right tradeoff between the completeness of the content and the visual message our end users could extract from it. Since the tool has been thought as a sensitization tool for young populations, we need to control the number of input classes, middle layers and output classes.

*Technologies and outcome* :

We have used D3.js as the main framework for this visualization. The interactivity offered by JavaScript allows us to display :
- The input classes : Car, Truck, Motorcycle, Bike, Pedestrian
- The middle layer : Death, harmed, unharmed
- The output layer : Wearing the security equipment or not

The supported interactions are the following :

![image](/Images/int_1.png)

This allows us to highlight the importance of wearing all the necessary security equipments. When the user hovers on a branch of the graph, this displays exact numbers about this branch. We also created filter buttons to allow the users to observe different scenarios (i.e on weather conditions or luminosity).

![image](/Images/sankey_final_weather.png)

Although we do believe that the design manages to display the right message, there are several limits that we would like to highlight :
- The complexity of the graph has been highly reduced in order to make it understandable for the end users
- The interaction is limited to the tooltip on the hover, and could be improved by showing additional middle layers when the user clicks on some buttons or activates some options
- We could develop another reading perspective on the same design by adding several buttons that allow to increasingly augment the complexity of the graph
- We could also use the notion of time to show how this graph has changed over time

### 2. Prevention

*Motivation* :

Can communes, departments, or even the state prevent crashes before they occur? To answer this vast question, we created a graph whose role is to cluster the types of roads (width, surface, infrastructure, proximity of a school…), and their related accident rate, thanks to a T-SNE embedding. We reduce dimension to allow the user to visualize high dimensional problems in a simple dashboard. Thanks to this visualization, we expect road authorities to be able to adjust the characteristics of a road when building or renovating a road.

The user can select the type of road from the different pages(communal, departmental, national), and in each case, observe the clusters created by T-SNEs. The green clusters represent a low accident rate, and the red ones a high one. The user can hover on a given point to observe all the characteristics of a given road, and select a region in the T-SNE plot. When selecting a region, the histograms all around the plot are updated. This allows users to understand the local distributions of variables on which they can have an impact when building a new road.

*Design Sketch* :

Our initial sketch of the design looked like this :

![image](/Images/tsne.png)

The user can set some constraints, i.e environment linked constants that cannot be changed. On the other hand, he sets some variables (width of a road, speed, median strip width…). Based on these constraints and variables, we can compute a T-SNE embedding of the roads that share the same constraints. This way, the user is able to see where the profile of the manually specified road stands compared to other roads that share the same constraints.

Then, to explore and help his decision, we provide a tooltip that allows the user to display the information related to the road on the graph. The tooltip shows information about the characteristics of each road.
If the user observes that his road stands within a red region, i.e a large number of accident recorded since 2005, it should typically lead the user to challenge his initial hypothesis. In such case, our visualization tool would come as an exploration tool to see if there are some better characteristics that can be chosen among roads that share similar characteristics.

Finally, we provide the user a prediction of the accident profile of his road. We created a scale, that ranges from 1 to 5 and describes the cumulated amount of accidents. We chose to implement a Random Forest Classifier that is trained on the whole dataset. This additional information should simply relate a no-go scenario in case the accident profile is among the worst class for example. The accuracy achieved by this algorithm, although it’s not the main focus here, is a little higher than 66% in this 5-class framework.

*Technologies and outcome* :

We have used Altair as the main support for this graph. Altair offers a simple way to display tooltips, and offers a web support to export a graph in HTML format.

We decided to add interactivity at several levels :
- Through the tooltip
- Through the selection on the T-SNE
- By allowing the user to select the kind of road he’s interested in.

Indeed, we created three buttons (Communal, Departmental, State, Highway) so that the different users we are targeting can all filter the most relevant information quickly. We believe that this removes noise from other road types, and avoids to select filters manually.

We decided not to implement the accident rate prediction in the final version since it would have required a dedicated page on the website which kills a bit the interactivity. However, as we developped this design, an idea came to our mind. Instead of letting the user explore the tooltip in green or red regions, and try by himself to understand the distribution of parameters, why not use the T-SNE plot as a **trackpad** in which the user can select regions, and we then display histograms of the values of parameters in this region.

For example, here is the T-SNE embedding of all roads in France.

![image](/Images/tsne-final_2.png)

On this graph, we notice that several histograms are displayed around the T-SNE. The color scheme on the histogram gives us the contribution of each accident profile (from 1 to 5) to each histogram.

*Limits of the design* :

This design, due to its custom functionalities and quite original side, comes with several limitations :
- The main bias is that we have to think in terms of absolute number of accidents, since each record relates a single accident. However, there must be some dominant kind of roads in France, which means that it would be more relevant to think in terms of accident rate than absolute number of accidents
- There could be a cursor to show the evolution over time of this graph
- The T-SNE embedding cannot be used to make a fit-transform and cannot compute the embedding of additional points that the user would enter for example. Therefore, exploring other dimension reduction techniques such as PCA could help bring interactivity on this level. Moreover, the T-SNE embedding does not output the same graph at each run
- The data cleaning can be improved, by adding some outlier detection for example


### 3. Monitoring

*Motivation* :

The last task of road authorities is to monitor the roads, and the accident rates on each road. Additional security measures might be needed in certain cases, or certain conditions. Local authorities might have an idea of what kind of road is dangerous, but our visualization should bring a clear overall view, and allow the user to understand a high dimensional spatial problem and the distributions of several factors that act on the gravity of an accident.

We expect the user to select regions on the map of France, and see all the histograms being updated live. This can be useful to understand the distributions in a given region, and by navigating though the different tabs of the website, focus on the different types of roads.

A concrete way to apply the insights gained from this design would be for a department to take a look at the design on certain weather conditions, in certain luminance conditions, identify clusters, and decide to take special actions from this observation. It could mean additional security measures, reduced speed, radars…

*Design Sketch* :

Our initial sketch of the design looked like this :

![Initial map](/Images/initial_map.png)

The main feature was to visualize two maps at the same time, and the location of the accidents on the two maps according to filters. Instead of computing several graphs, all the information is loaded on a single graph. The filters are cumulative, which means that the users can explore the interactions between all filters.

*Technologies and outcome* :

We tried several implementations, including with [Folium map plotting tool](https://python-visualization.github.io/folium/), or with Altair. However, there seemed to be no great tool for webapps. For this reason, we switched a bit the concept of the graph, although a great interactive tool is present in the `graph3-monitoring` Monitoring notebook.

We then decided to re-use the idea of having a central trackpad which would be a 2D representation of the dataset, and understand the distributions around it. For the monitoring part, the spatial representation is an obvious choice. Therefore, we have a map of France in the center, and live updated histograms on the side that react to the regions the user selects on the map.

Since this is a monitoring tool, we expect the gravity of the accident to be at the core of any decision being taken. For this reason, we decided to encode the color scheme depending on the gravity of the accidents.

![image](/Images/map_final.png)

*Limits of the design* :

The design is interesting and we believe can bring value to authorities in charge of these questions. However, it suffers from some limitations :
- The data source is updated once a year only, which means that the data of year 2019 are not present at all.
- We could add buttons allowing the user to zoom on a department or a commune for example

## IV. Contributors

<table><tr><td align="center">
<a href="https://github.com/Anatoli-deBRADKE">
<img src="https://avatars1.githubusercontent.com/u/43547776?v=4" width="100px;" alt="Anatoli-deBRADKE"/>
<br />
<sub><b>Anatoli-deBRADKE</b></sub>
</a><br /></td>
<td align="center"><a href="https://github.com/maelfabien"><img src="https://avatars0.githubusercontent.com/u/24256555?v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>maelfabien</b></sub>
</a><br /></td>
<td align="center"><a href="https://github.com/RaphaelLederman"><img src="https://avatars2.githubusercontent.com/u/38351531?v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>RaphaelLederman</b></sub>
</a><br /></td>
<td align="center"><a href="https://github.com/AlexPeterBec"><img src="https://avatars0.githubusercontent.com/u/10231302?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>AlexPeterBec</b></sub>
</a><br /></td>
<td align="center"><a href="https://github.com/AnthonyHoudaille"><img src="https://avatars3.githubusercontent.com/u/31823617?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>AnthonyHoudaille</b></sub>
</a><br/></td>

</tr></table>
