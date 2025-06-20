##Eurovision Winners Dashboard

This project was created as a final assignment for Lesson 14 of the Code the Dream Data Engineering course.

It includes web scraping, data cleaning, database import, SQL queries, and a Streamlit dashboard based on the Eurovision Song Contest winners data from Wikipedia.

#Project Features:
	•	Web Scraping: Automatically extracts Eurovision winners using Selenium.
	•	Data Cleaning & Transformation: Extracted data is cleaned and saved in CSV format.
	•	Database Integration: Data is stored in a SQLite database (eurovision.db).
	•	SQL Querying: You can query the database for insights like top countries by wins.
	•	Interactive Dashboard: Built with Streamlit, allows filtering by decade and country, and displays:
	•	Top 10 countries with the most wins
	•	Winners by decade
	•	Multiple-time winning artists
	•	Countries with no wins

#Files:
	•	eurovision_scraper.py – scrapes data from Wikipedia
	•	import_to_db.py – loads data from CSV to SQLite database
	•	query_db.py – runs example SQL queries
	•	dashboard.py – Streamlit dashboard
	•	eurovision_winners.csv – cleaned dataset
	•	eurovision.db – SQLite database
	•	requirements.txt – dependencies
