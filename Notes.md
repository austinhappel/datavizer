# Datavizer notes

# Overview

* Users can create many **datasets**
* Users can create many **data visualizations**
* Datasets contain many **datum** units
* A datum has only one **data type**
* A data type contains a series of customizable **fields** that determine its **schema**


# Users

* Users can customize a data type through an administration tool
* Users have a personal page that displays a list of all their **data sets** and **data visualizations**
* There will be a stock set of default **data visualization templates** a user can use
* Users will be able to **customize** their data **visualizations**
    * form fields
* Users can reset their password
* Users will get a **confirmation email** when they first sign up
    * They will be required to **click the confirmation link** in this email before they are allowed to log in.


# Visualization items

* A **data visualization** is displayed on a single, unique page specific to the visualization
* Visualization can be flagged as **public or private**
    * Public visualizations may be displayed on the **home page**
* A **custom url** will be provided in the admin form for the visualization
    * `/user/visualization-name-<n>`


# Datasets

* For every dataset created, datavizer will **provide a basic, rate limited API** that the user can query.
    * Will support JSON and JSONP
