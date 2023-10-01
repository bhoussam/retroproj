import pandas as pd
import streamlit as st

if 'wish' not in st.session_state:
    st.session_state["wish"] = pd.DataFrame(
        {
            "user": [""],
            "film": [""]
        }
    )

st.session_state['wish'] = st.data_editor(st.session_state["wish"], use_container_width=True, num_rows='dynamic')
wish_films = st.session_state['wish']['film'].str.upper()
base_films = st.session_state['base']['films'].str.upper()

union = st.session_state['base'][base_films.isin(wish_films)]

st.dataframe(union, use_container_width=True)