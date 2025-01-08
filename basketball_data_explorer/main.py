import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="NBA Player Stats Explorer", layout="wide")
st.title("NBA Player Stats Explorer")

st.markdown("""
This app was created by **Radosav Panic** and performs web scraping of NBA player stats data.
* **Data source:** [basketball-reference.com](https://www.basketball-reference.com)
""")

st.sidebar.header("User Input Features")
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2026))))

# Web scraping of NBA player stats
@st.cache_data
def load_data(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    df = df.drop(columns=['Awards'], errors='ignore')
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

playerstats = load_data(selected_year)

# Team Selection sidebar
sorted_unique_team = sorted(playerstats.Team.astype(str).unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Position Selection sidebar
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data based on team and position
df_selected_team = playerstats[(playerstats.Team.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

# Reset index to start from 1 (instead of 0) in table
df_selected_team = df_selected_team.reset_index(drop=True)
df_selected_team.index += 1

st.header('Diplay Player Stats of Selected Team(s)')
st.write(f'Table size: {str(df_selected_team.shape[0])} rows and {str(df_selected_team.shape[1])} columns.')
st.dataframe(df_selected_team, height=600)

# Download NBA Player stats data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats_{selected_year}.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if "show_heatmap" not in st.session_state:
    st.session_state.show_heatmap = False

if st.button('Intercorrelation Heatmap'):
    st.session_state.show_heatmap = not st.session_state.show_heatmap

if st.session_state.show_heatmap:
    st.header('Intercorrelation Matrix Heatmap')

    numeric_df = df_selected_team.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()  # Calculate correlation matrix

    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        sns.set(font_scale=0.8)
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True, cmap="coolwarm", cbar_kws={"shrink": 0.5})
    st.pyplot(f)
