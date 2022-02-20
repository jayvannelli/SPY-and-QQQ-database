import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

holdings = open('data/spyHoldings.csv').readlines()

for holding in holdings[1:]:
    counter = 0
    tickers = [holding.split(',')[1].strip()]
    stock_names = [holding.split(',')[0].strip()]
    sector = [holding.split(',')[-4].strip()]
    asset_weighting = [holding.split(',')[4]]
    cursor.execute("INSERT INTO spy_holdings (symbol, company, sector, weighting) VALUES (?, ?, ?, ?)", (tickers[counter], stock_names[counter], sector[counter], asset_weighting[counter]))
    counter += 1

connection.commit()