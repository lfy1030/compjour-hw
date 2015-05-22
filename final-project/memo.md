# Final Project Pitch Memo

## Quick Pitch

[Minna no Data](http://www.minnanods.net/) is a crowdsourciing site in Japan that gathers and display on their website a searchable database of measurements of radioactive substances in food products. The measurements are submitted by various local NGOs, NPOs and community volunteer groups from around Japan and checked and entered into the database by the website organizers. 

## The Old Way

In order to access the data now, you have to nagivate to the page that allows you to select from four categories: by prefecture, by type of food, by the season of the food and by date. 

After going to the category, you then have to go to individual pages to view data for the subcategories (e.g. Spring, Winter, Autumn, Summer). You cannot view data from different subcategories in the same page. There are also no way of checking an entry across categories. (e.g. in the Seasonal Food category pages you cannot see what food type a particular entry belongs to)

The data is available in a single table. It can be filtered and sorted by parameters such as product name, date of measurement, location, etc, but that is all. There is no visualization on the data and you really cannot tell anything from it. 

## The New Way

I intend to make visualizations for the data, and also add on the subcategories as tags to the data point. For example, if something belows to the Vegetable category and the Spring category, they should have both as attributes mapped to the ID of the data point so that the categories will no longer be separated from one another. 

## Data Source and Collection 

As mentioned above the data comes from crowdsourced food data site [Minna no Data](http://www.minnanods.net/). Unfortunately they do not release the CSVs for their data as of now. However, the html for their data pages are fairly well-formatted, so I intend to just scrape them from the web pages. 

## Data-Cleaning and Processing 

I will convert the data from their html table form back into probably a python dict and store it as a json file. Alternatively it could also be converted into a csv. I plan to tag them by categories while I am converting them into the stored data format based on which category pages I'm extracting the data from as the Seasonal and Food type data points are missing. The two category types should be mergeable because although not shown in the webpage there is an ID attached to each data point. 

## Data Storage

Either json or csv. Most likely json I think. 

## Who else has done it? 

I don't think anyone else has tried working with this set of data because it's a bit obscure and also not downloadable as json or csv or some sort of data format. 

## Pre-mortem

I intend to use Google Translate for webpages to translate the entry names in Japanese. It is fairly accurate. If the plug-in/widget doesn't work then it won't be translated unless I have spare time. 

The tagging process may be more difficult than anticipated, in which case I may leave out the tagging first and finish putting up datapoints by data and location, and then add on the Season and Food Types later. 