# Web Scraping - Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)

In this project, I built a web application that scrapes various NASA websites for data related to the Mission to Mars and displays the information in a single HTML page. Scraped data is inserted to Mongo database before being used. Here are the steps followed:


## Step 1 - Scraping

The following websites were scraped using BeautifulSoup, Pandas, and Splinter


* [NASA Mars News Site](https://mars.nasa.gov/news/) was scraped for the latest News Title and Paragraph Text. 

* JPL Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) was scraped for a Mars image. A random image was picked for the HTML page.

* Mars Facts webpage [here](https://space-facts.com/mars/) was scraped using Pandas for the table containing facts about the planet including Diameter, Mass, etc.

* USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) was scraped to obtain high resolution images for each of Mars hemispheres.

- - -

## Step 2 - MongoDB and Flask Application

* MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs above.

* The database is only inserted a single dictionary combining all the scraped data. 

- - -

## Step 3 - HTML

* Bootstrap and Jinja were used to structure the HTML template.


#### Copyright

This notebook was completed as part of Data Analytics Bootcamp offered by Trilogy Education Services © 2020. 
