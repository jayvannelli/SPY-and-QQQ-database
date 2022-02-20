import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

holdings = open('data/qqqHoldings.csv').readlines()

for holding in holdings[1:]:
    counter = 0
    tickers = [holding.split(',')[2].strip()]
    stock_names = [holding.split(',')[-4].strip()]
    sector = [holding.split(',')[-2].strip()]
    asset_weighting = [holding.split(',')[-5]]
    cursor.execute("INSERT INTO qqq_holdings (symbol, company, sector, weighting) VALUES (?, ?, ?, ?)", (tickers[counter], stock_names[counter], sector[counter], asset_weighting[counter]))
    counter += 1

connection.commit()