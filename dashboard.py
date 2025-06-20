# dashboard.py
import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.title("Eurovision Song Contest Insights")

# Load data
df = pd.read_csv("eurovision_winners.csv")

# Sidebar Filters
st.sidebar.header("Filters")

# Decade filter
df['Year'] = df['Year'].astype(int)
df['Decade'] = (df['Year'] // 10) * 10
decade = st.sidebar.selectbox("Select a decade:", sorted(df['Decade'].unique()))
filtered_df = df[df['Decade'] == decade]

# Country filter
country = st.sidebar.selectbox("Select a country (optional):", ["All"] + sorted(df['Country'].unique()))
if country != "All":
    filtered_df = filtered_df[filtered_df['Country'] == country]

# Top countries by number of wins
st.subheader("Top 10 Countries by Number of Wins")
country_wins = df['Country'].value_counts().reset_index()
country_wins.columns = ['Country', 'Wins']
fig1 = px.bar(country_wins.head(10), x='Country', y='Wins', color='Wins', title="Top 10 Winning Countries")
st.plotly_chart(fig1)

# Winners by selected decade
st.subheader(f"Winners in the {decade}s")
st.dataframe(filtered_df[['Year', 'Country', 'Song', 'Artist']])

# Repeat winners
st.subheader("Multiple-Time Winners")

# Count artists
artist_counts = df['Artist'].value_counts()
repeats = artist_counts[artist_counts > 1].index.tolist()

if repeats:
    for artist in repeats:
        st.markdown(f"**{artist}** — {artist_counts[artist]} wins")
        artist_df = df[df['Artist'] == artist][['Year', 'Country', 'Song']]
        artist_df.index = range(1, len(artist_df) + 1)  # Start index from 1
        st.dataframe(artist_df)
else:
    st.write("There are no artists with more than one win.")

# Countries with the Fewest Wins (show all with the minimum number of wins)
st.subheader("Countries with the Fewest Wins")

country_win_counts = df['Country'].value_counts()

min_wins = country_win_counts.min()

fewest_wins = country_win_counts[country_win_counts == min_wins]

countries_line = ', '.join([f"{country} ({wins})" for country, wins in fewest_wins.items()])

st.write(countries_line)


# Assume you have a full list of participating countries:
all_countries = [
    "Switzerland", "Netherlands", "France", "Luxembourg", "Italy", "Austria", "United Kingdom", "Spain",
    "Monaco", "Ireland", "Sweden", "Germany", "Belgium", "Israel", "Norway", "Turkey", "Greece", "Ukraine",
    "Russia", "Denmark", "Finland", "Portugal", "Estonia", "Latvia", "Azerbaijan", "Serbia", "Georgia",
    "Australia", "Croatia", "Poland", "Czech Republic", "Slovenia", "Slovakia", "Romania", "Bulgaria",
    "Lithuania", "Armenia", "Malta", "Cyprus", "Albania", "North Macedonia", "Iceland", "Moldova", "Hungary",
    "San Marino", "Montenegro", "Andorra", "Bosnia and Herzegovina", "Belarus"
]

won_countries = df['Country'].unique().tolist()
no_win_countries = sorted(set(all_countries) - set(won_countries))

if no_win_countries:
    st.write("Countries that have never won Eurovision:")
    st.write(", ".join(no_win_countries))
else:
    st.write("All countries in the list have at least one win.")

# Footer
st.markdown("---")
st.markdown("Final Project · Code the Dream · Created by **Mariya Doronkina**")