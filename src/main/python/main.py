import streamlit as st
from scraping.scraper import populate_df

df = populate_df()

st.dataframe(df, use_container_width=True)