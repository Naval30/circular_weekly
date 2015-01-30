*****   HOW TO RUN THE SPIDER *****

To run the spider for a store and a store location we do:
scrapy crawl <spider name> -a zip_code=<zip_code>

<spider name> = the name of the spider for the store we are
scraping data. ex: stopandshop (spider for Stop and Shop)

<zip_code> = 5 digit zipcode of the store location we are
scraping the data for. ex: 10461 (Bronx zipcode)

ex: scrapy crawl stopandshop -a zip_code=10461

