import sqlite3

conn = sqlite3.connect("eurovision.db")
cursor = conn.cursor()

query = """
SELECT Country, COUNT(*) as Wins
FROM winners
GROUP BY Country
ORDER BY Wins DESC
LIMIT 10;
"""

results = cursor.execute(query).fetchall()
print("Top 10 countries by wins:")
for row in results:
    print(row)

conn.close()