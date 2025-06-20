from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/List_of_Eurovision_Song_Contest_winners")

print(driver.title)

table = driver.find_element(By.CLASS_NAME, "wikitable")
rows = table.find_elements(By.TAG_NAME, "tr")

data = []
for row in rows[1:]:
    year_cell = row.find_elements(By.TAG_NAME, "th")
    cols = row.find_elements(By.TAG_NAME, "td")

    if len(year_cell) == 1 and len(cols) >= 4:
        year = year_cell[0].text.strip().split("\n")[0]
        country = cols[0].text.strip()
        song = cols[1].text.strip().strip('"')
        artist = cols[2].text.strip()
        data.append([year, country, song, artist])

with open("eurovision_winners.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Year", "Country", "Song", "Artist"])
    writer.writerows(data)

print("CSV file saved: eurovision_winners.csv")
driver.quit()