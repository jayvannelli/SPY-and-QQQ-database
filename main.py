import sqlite3

#Connect to the empty sqlite3 database 
connection = sqlite3.connect('app.db')
cursor = connection.cursor()

#List off the tickers of the index funds we are going to track
index_funds = ['QQQ', 'SPY']

#Enter into a loop for each entity inside the above mentioned array of funds
for fund in index_funds:
    if fund == 'QQQ':
        individual_fund_name = 'QQQholdings'
        #Opens and reads the lines of the corresponding csv file (wwithin the data folder) and create a new db if one does not exist
        holdings = open('data/qqqHoldings.csv').readlines()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {} (
                            "id" INTEGER PRIMARY KEY,
                            "symbol" TEXT NOT NULL UNIQUE,
                            "company" TEXT NOT NULL,
                            "sector" TEXT,
                            "weighting" TEXT 
                        )'''.format(individual_fund_name))
        #For each holding (line) in the csv file, find the corresponding data that matches wwith the sections we want to obtain for each holding
        for holding in holdings[1:]:
            counter = 0
            tickers = [holding.split(',')[2].strip()]
            stock_names = [holding.split(',')[-4].strip()]
            sector = [holding.split(',')[-2].strip()]
            asset_weighting = [holding.split(',')[-5]]
            #Insert the data of each ticker into the newly made database until there are no more lines in the csv to read
            cursor.execute("INSERT INTO QQQholdings (symbol, company, sector, weighting) VALUES (?, ?, ?, ?)", (tickers[counter], stock_names[counter], sector[counter], asset_weighting[counter]))
            counter += 1
    else:
        #The same process detailed above will happen for the next holding in the "index_funds" array
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