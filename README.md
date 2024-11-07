# Wikipedia_Scraper
This project retrieves data about world leaders from an API and scrapes Wikipedia pages for additional information. It uses the requests library to interact with the API and BeautifulSoup for web scraping to get relevant paragraphs from Wikipedia.
There are two versions of the project:

Version 1: Uses threads to run multiple scraping tasks at the same time. It prints the results as it goes.

Version 2: Runs the scraping without threads and returns the results without printing them.


Ecco una versione più semplice della descrizione:

Description
This project has two main parts:

API Interaction: The first part gets information about countries and their leaders from an API (https://country-leaders.onrender.com). It uses a cookie to access data about leaders from different countries.

Web Scraping: The second part uses BeautifulSoup to scrape the first paragraph from Wikipedia pages of political leaders. The function get_first_paragraph gets the first paragraph of a Wikipedia page, cleans the text, and returns it.

There are two versions of the project:

Version 1: Uses threads to run multiple scraping tasks at the same time. It prints the results as it goes.

Version 2: Runs the scraping without threads and returns the results without printing them.

Libraries Used:
    requests: To make HTTP requests.
    json: For working with JSON data.
    BeautifulSoup: For scraping and parsing web pages.
    threading: For running tasks at the same time (used in Version 1)