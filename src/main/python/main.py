import streamlit as st
from scraping.scraper import populate_df

st.set_page_config(
    page_title="HOME",
    layout="wide"
)

if 'base' not in st.session_state:
    st.session_state['base'] = None

if 'user' not in st.session_state:
    st.session_state['user'] = ""

user = st.text_input("Slt t ki ???", value="")
if user:
    st.session_state['user'] = user

if st.session_state['user']:
    st.session_state['base'] = populate_df()
    st.dataframe(st.session_state['base'], use_container_width=True)
