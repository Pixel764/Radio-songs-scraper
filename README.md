# Radio-songs-scraper

Scrape data from page and save in **MySQL**
<br>
<br>
**Songs are scraped from** -> https://www.bbc.co.uk/sounds/play/live:bbc_6music <br>
**Scraped Data:** Song title , Song Artist <br>

## Conf
Create `.env` file.

Your `.env` file should look like:
> DB_USER = MySQLuser <br>
> DB_PASSWORD = MySQLpassword <br>
> DB_HOST = localhost <br>
> DB_TITLE = your_dbTitle <br>
> SCRAPE_TIME = Seconds <br>


## Start
- Run virtual enviroment
> pipenv shell
<br>

- Install requirements
> pipenv install

- Create Database (If you first time run script)
> python main.py create_database <br>

Database will be created with the title from `.env` <br>

Check `logs.txt`
<br>

- Run script
> python main.py <br>

Now every **SCRAPE_TIME** web-page will be scraped.<br>
Status of every scrape will be in `logs.txt`
<br>
<br>
Script will add only new data!

