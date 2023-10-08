import pandas as pd
import streamlit as st
import os

csv_path = "data/{}.csv".format(st.session_state['user'])
if st.session_state['user']:
    if os.path.exists(csv_path):
        wish = pd.read_csv(csv_path)

        wish_films = wish['film'].str.upper()
        base_films = st.session_state['base']['films'].str.upper()

        union = st.session_state['base'][base_films.isin(wish_films)]

        st.dataframe(union, use_container_width=True)
