import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

index_funds = ['QQQ', 'SPY']

for fund in index_funds:
    if fund == 'QQQ':
        individual_fund_name = 'QQQholdings'
        holdings = open('data/qqqHoldings.csv').readlines()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {} (
                            "id" INTEGER PRIMARY KEY,
                            "symbol" TEXT NOT NULL UNIQUE,
                            "company" TEXT NOT NULL,
                            "sector" TEXT,
                            "weighting" TEXT 
                        )'''.format(individual_fund_name))
        for holding in holdings[1:]:
            counter = 0
            tickers = [holding.split(',')[2].strip()]
            stock_names = [holding.split(',')[-4].strip()]
            sector = [holding.split(',')[-2].strip()]
            asset_weighting = [holding.split(',')[-5]]
            cursor.execute("INSERT INTO QQQholdings (symbol, company, sector, weighting) VALUES (?, ?, ?, ?)", (tickers[counter], stock_names[counter], sector[counter], asset_weighting[counter]))
            counter += 1
    else:
        individual_fund_name = 'SPYholdings'
        holdings = open('data/spyHoldings.csv').readlines()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {} (
                            "id" INTEGER PRIMARY KEY,
                            "symbol" TEXT NOT NULL UNIQUE,
                            "company" TEXT NOT NULL,
                            "sector" TEXT,
                            "weighting" TEXT 
                        )'''.format(individual_fund_name))
        for holding in holdings[1:]:
            counter = 0
            tickers = [holding.split(',')[1].strip()]
            stock_names = [holding.split(',')[0].strip()]
            sector = [holding.split(',')[-4].strip()]
            asset_weighting = [holding.split(',')[4]]
            cursor.execute("INSERT INTO SPYholdings (symbol, company, sector, weighting) VALUES (?, ?, ?, ?)", (tickers[counter], stock_names[counter], sector[counter], asset_weighting[counter]))
            counter += 1

connection.commit()