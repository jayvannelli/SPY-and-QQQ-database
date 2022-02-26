This is my first time using SQL to create a database, and in this case I made one for the SPDR® S&P 500® ETF Trust ($SPY) and one for the Invesco QQQ Trust ($QQQ).
By downloading their holdings directly to a csv file and storing that locally, I was able to write a python script that parsed through that data and created
an independant database with each holdings ticker, company name, sector and weighting. I will further elaborate on this project to include auto-updating scripts that
download the latest holdings filing to add, update and remove the necessary information and stay as up to date as possible.

The "data" folding consists of the latest holdings excel sheet (pulled directly from the given etf site)
