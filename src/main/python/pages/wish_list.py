import pandas as pd
import streamlit as st
import os

if 'wish' not in st.session_state:
    st.session_state['wish'] = None

if st.session_state['user']:

    st.write("Salut {}".format(st.session_state['user']))

    csv_path = "data/{}.csv".format(st.session_state['user'])
    if os.path.exists(csv_path):
        st.session_state['wish'] = pd.read_csv(csv_path)
    else:
        st.session_state['wish'] = pd.read_csv(st.file_uploader("Charge ta wish list ici BG"))
        st.session_state['wish'].to_csv(csv_path, index=False)

    st.session_state['wish'] = st.data_editor(st.session_state['wish'], use_container_width=True, num_rows='dynamic')

    edit = st.button("Sauvegarde ta wish list BG")
    if edit:
        st.session_state['wish'].to_csv(csv_path, index=False)


