# Information Visualization

<img alt="GitHub followers" src="https://img.shields.io/github/followers/maelfabien.svg?style=social"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/maelfabien/DataVisualization.svg"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/maelfabien/DataVisualization.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/3.svg">

![image](/Images/demo.gif){:width="100%"}

## I. Project description

**Contributors : Anatoli de Bradké, Raphael Lederman, Alexandre Bec, Anthony Houdaille, Maël Fabien**

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

To set the context, there are several visualizations that we present in this section : https://infoviz.onrender.com/?all=The+Data

- Age of the victime and Number of accidents per day in France :

![image](/Images/ts_2.png)

- Time of the accidents and Location of the accidents :

![image](/Images/loc_2.png)


## III. Designs

Our analysis could bring value to several road authorities in France :
- Communes, that are in charge of communal roads
- Departments, that are in charge of departmental roads
- The state, in charge of the national roads
- Private companies (Vinci) in charge of Highways

We except our end users to use our tool to :
- **Sensitize** the youngsters and road criminals on the danger of the roads depending on the transportation mode they are using.
- **Prevent** road dangers through a tool that would advise the best road characteristics for a road rehabilitation, and visually illustrate the outcome of the algorithm
- **Monitor** the dangers of the roads (at difference scales, including Communes, Departments and Nation) by allowing the user to select geographic zones and filters (weather conditions, hour of the day…) to gain additional insights

For this reason, we subdivided our website into several sections (Data exploration, All roads, Communal, Departmental, National, and highway roads) and in each case, Sensitize, Prevent and Monitor sections.

### 1. Sensitization

*Motivation* :

Local police and communes are working together on sensitization of the youngster on the road dangers. One might believe that dangers for these kids arise once they have their first motorcycle or car. However, if they are involved in an accident, death rates among bike riders and pedestrians are incredibly high compared to other transportation means.

We selected a Sankey diagram (flow chart) to illustrate the dangers of the road, not only for car users, but also for pedestrians, bike riders or motorcyclists. The aim of this design is to convey a simple, easily understandable yet visually efficient message.

*Design sketch* :

Our initial sketch of the design looked like this :

![image](/Images/sankey.png)

We intend to support a filter on the type of roads (communal, departmental, national), and to observe the difference of survival rate of the different categories of road users depending on the speed on the road. This would illustrate how the speed of a car impacts the survival rate of the other road users.

The design helps the reader understand the distribution of the volume of road users accident, depending on the kind of road being used, as well as the effect of speed.

*Data processing and challenges* :

One of the challenges is that each database (vehicle, passengers/pedestrians, location, characteristic) does not share a common key to join them. Indeed, the vehicle database distinguishes every vehicle implied in a same crash, whereas the characteristics of an accident only reports one observation for this specific case. On the other hand, the pedestrians and bike riders only appear in the passenger database. Overall, some data processing was needed in order to build a complete table.

Then, one of the other challenges was to find the right tradeoff between the completeness of the content and the visual message our end users could extract from it. Since the tool has been thought as a sensitization tool for young populations, we need to control the number of input classes, middle layers and output classes.

*Technologies and outcome* :

We have used Plotly as the main framework for this visualization. The interactivity offered by the JavaScript behind Plotly allow us to display :
- The input classes : Car, Truck, Motorcycle, Bike, Pedestrian
- The middle layer : Wearing the security equipment or not
- The output layer : Death, harmed, unharmed

This also allows us to highlight the importance of wearing all the necessary security equipments. When the user clicks on a branch of the graph, this highlights the values of this branch specifically, and displays in a tooltip additional information and exact numbers about this branch.

![image](/Images/sankey_final_2.png)

Although we do believe that the design manages to display the right message, there are several limits that we would like to highlight :
- The complexity of the graph has been highly reduced in order to make it understandable for the end users
- The interaction is limited to the tooltip on the hover, and could be improved by showing additional middle layers when the user clicks on some buttons or activates some options
- We could develop another reading perspective on the same design by adding several buttons that allow to increasingly augment the complexity of the graph
- We could also use the notion of time to show how this graph has changed over time

### 2. Prevention

*Motivation* :

There are critical decisions taken by road authorities when it comes road rehabilitation or construction. It is indeed necessary to choose the width of the road, the turn angle, the speed of the road, whether the road should have a median strip or not… All these decisions can have a large impact on the future accident profile of this road. Although road authorities in France are used to exploit the datasets we are presenting, we believe that a design that allows them to observe the accident profile of similar roads could be a great decision support tool.

Our aim is also to develop a Machine Learning model able to predict the accident profile of a road given its characteristics. Overall, if our design is successful, it should help prevent some accidents linked to profiles of roads. The main point of embedding is to unlock insights on high dimensional problems.

*Design Sketch* :

Our initial sketch of the design looked like this :

![image](/Images/tsne.png)

The user is able to set some constraints, i.e environment linked constants that cannot be changed. On the other hand, he sets some variables (width of a road, speed, median strip width…). Based on these constraints and variables, we can compute a T-SNE embedding of the roads that share the same constraints. This way, the user is able to see where the profile of the manually specified road stands compared to other roads that share the same constraints.

Then, to explore and help his decision, we provide a tooltip that allows the user to display the information related to the road on the graph. The tooltip shows information about the characteristics of each road.
If the user observes that his road stands within a red region, i.e a large number of accident recorded since 2005, it should typically lead the user to challenge his initial hypothesis. In such case, our visualization tool would come as an exploration tool to see if there are some better characteristics that can be chosen among roads that share similar characteristics.

Finally, we provide the user a prediction of the accident profile of his road. We created a scale, that ranges from 1 to 5 and describes the cumulated amount of accidents. We chose to implement a Random Forest Classifier that is trained on the whole dataset. This additional information should simply relate a no-go scenario in case the accident profile is among the worst class for example. The accuracy achieved by this algorithm, although it’s not the main focus here, is a little higher than 52% in this 5-class framework.

*Technologies and outcome* :

We have used Altair as the main support for this graph. Altair offers a simple way to display tooltips, and offers a web support to export a graph in HTML format.
We decided to add interactivity at several levels :
- Through the tooltip
- By allowing the user to select the kind of road he’s interested in.

Indeed, we created three buttons (Communal, Departmental, State) so that the different users we are targeting can all filter the most relevant information quickly. We believe that this removes noise from other road types, and avoids to select filters manually. For example, here is the T-SNE embedding of the communal roads in France.

![image](/Images/tsne-final_2.png)

The blue dot corresponds to the user’s input. We observe in this case that it is among the worse class. If the user wants to optimize the accident profile of the road, he might be interested in exploring the points at the green limit or at the orange limit.

*Limits of the design* :

This design, due to its custom functionalities and quite original side, comes with several limitations :
- The main bias is that we have to think in terms of absolute number of accidents, since each record relates a single accident. However, there must be some dominant kind of roads in France, which means that it would be more relevant to think in terms of accident rate than absolute number of accidents
- There could be a cursor to show the evolution over time of this graph
- The interactivity could be improved to allow, for example, the user to add new points on the map
- The algorithm could output a single best road that is the closest (in terms of distance on the T-SNE map) to the input road characteristics
- The T-SNE embedding cannot be used to make a fit-transform and cannot compute the embedding of additional points. Therefore, exploring other dimension reduction techniques such as PCA could help bring interactivity on this level. Moreover, the T-SNE embedding does not output the same graph at each run
- The data cleaning can be improved, by adding some outlier detection for example


### 3. Monitoring

*Motivation* :

Monitoring the number of accidents on roads is not an easy task. Communes and departments might be aware of roads in which there are empirically more accidents. However, it might become really hard to deal with the large amount of variables observed at each accident : weather conditions, hour of the day, number of passengers… Moreover, it is really hard to visualize the accident profile of roads at different scales (a single commune, or the whole state), compared to other places (how does a commune perform compared to another), over time (year by year) given filters.

For this reason, we wanted to develop a tool that looks really simple at first sight, i.e two maps and a set of filters.  This tool is however really powerful, since it covers all the needs described above. The user can set filters and observe the interaction between them. For example, the  end user will be able to monitor the accidents that occurred during the night, implied male drivers, with snowy conditions, at the level of his commune or of the department for example.

The filters can be : night vs.day, death vs. unharmed, weather condition, year, sex of the driver… The main idea behind such a complete tool is to allow authorities to gain insights on a large dimensional problem, with cumulative filters : for example, deaths on snowy days, by night, since 2005. Clusters can then be visually defined, and actions can be taken from this perspective.

A concrete way to apply the insights gained from this design would be for a department to take a look at the design on certain weather conditions, in certain luminance conditions, identify clusters, and decide to take special actions from this observation. It could mean additional security measures, reduced speed, radars…

*Design Sketch* :

Our initial sketch of the design looked like this :

![Initial map](/Images/initial_map.png)

The main feature is to visualize two maps at the same time, and the location of the accidents on the two maps according to filters. The interesting point it to be able to compare different scales and how they react to filters :
- Commune vs. Commune
- Commune vs. department
- Commune vs. Region
- Commune vs. state
- Department vs. region
- Department vs. state
- Region vs.state

Instead of computing several graphs, all the information is loaded on a single graph. The filters are cumulative, which means that the users can explore the interactions between all filters.

Since we have a lot of features, it was tempting to display them in additional dimensions instead of filters. We could play on the size of dots, on their color, on the marker, on the angle of the marker… In the end, the user would have surely been lost, which is the reason why we chose filters.

*Data processing and challenges* :

For this visualization, we focus on the characteristics dataset. Many entries in
the characteristics dataset do not contain GPS coordinates. These observations
had to be removed, in most cases, more than 50% of the data does not contain GPS coordinates.

Then, some outliers were located in Switzerland for example or in neighboring
countries. We also removed those points. We also chose to only focus on the
metropolitan area, and exclude the DOM-TOM of our analysis.

We also expect the user to use the tooltip provided to get the micro-macro view
and explore the details of a single accident if needed.

*Technologies and outcome* :

We use [Folium map plotting tool](https://python-visualization.github.io/folium/)
as our main framework. Folium is lightweight and relatively easy to configure in Python,
and has some good interactive features,
it provides a dynamic map where the user can zoom in & out to focus on specific
areas. We included a tooltip on click with details about the accident.

In the end, we built an exploration tool with a high level of specificity on the
data to display. Here are the filters offered by the tool in the notebook :

<img src="/Images/filter_buttons.png" alt="Buttons image" width="700"/>

As Folium supports HTML exports, we extracted some key views to display on our
web interface for demonstration.

*Limits of the design* :

The design is interesting and we believe can bring value to authorities in charge of these questions. However, it suffers from some limitations :
- The data source is updated once a year only, which means that the data of year 2019 are not present at all.
- The interactivity remains limited due to the dataset size. Having filters means we have a very large dataset at the beginning. Therefore, the full dataset cannot be embedded in a web application.
- Filters list can be extended to interact with every parameter available, but there would be too much of parameters.

## IV. Contributors

<table><tr><td align="center">
<a href="https://github.com/Anatoli-deBRADKE">
<img src="https://avatars1.githubusercontent.com/u/43547776?v=4" width="100px;" alt="Anatoli-deBRADKE"/>
<br />
<sub><b>Anatoli-deBRADKE</b></sub>
</a><br /><a href="https://github.com/maelfabien/DataViz/commits?author=Anatoli-deBRADKE" title="Code">💻</a></td>
<td align="center"><a href="https://github.com/maelfabien"><img src="https://avatars0.githubusercontent.com/u/24256555?v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>maelfabien</b></sub>
</a><br /><a href="https://github.com/maelfabien/DataViz/commits?author=maelfabien" title="Code">💻</a></td>
<td align="center"><a href="https://github.com/RaphaelLederman"><img src="https://avatars2.githubusercontent.com/u/38351531?v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>RaphaelLederman</b></sub>
</a><br /><a href="https://github.com/maelfabien/DataViz/commits?author=RaphaelLederman" title="Code">💻</a></td>
<td align="center"><a href="https://github.com/AlexPeterBec"><img src="https://avatars0.githubusercontent.com/u/10231302?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>AlexPeterBec</b></sub>
</a><br /><a href="https://github.com/maelfabien/DataViz/commits?author=AlexPeterBec" title="Code">💻</a></td>
<td align="center"><a href="https://github.com/AnthonyHoudaille"><img src="https://avatars3.githubusercontent.com/u/31823617?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>AnthonyHoudaille</b></sub>
</a><br /><a href="https://github.com/maelfabien/DataViz/commits?author=AnthonyHoudaille" title="Code">💻</a></td>

</tr></table>
