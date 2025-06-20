import sqlite3
import pandas as pd

df = pd.read_csv("eurovision_winners.csv")

conn = sqlite3.connect("eurovision.db")

df.to_sql("winners", conn, if_exists="replace", index=False)

print("Imported to database. First 5 rows:")
print(pd.read_sql("SELECT * FROM winners LIMIT 5", conn))

conn.close()