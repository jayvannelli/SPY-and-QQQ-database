import sqlite3

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

cursor.execute("""
    #SELECT symbol FROM qqq_holdings
""")

#This requires a contsant flow of updated holding to the qqq_holding.csv file in the directory
holdings = open('data/qqqHoldings.csv').readlines()
rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]
t = [holding.split(',')[2].strip() for holding in holdings][1:]

for sym in t:
    try:
        if sym not in symbols:
            print(f"Added a new stock {sym}")
    except Exception as e:
        print(sym)
        print(e)