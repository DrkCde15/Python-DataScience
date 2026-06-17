import pandas as pd
import streamlit as st

@st.cache_data
def load_data(upload):

    extension = upload.name.split('.')[-1].lower()

    if extension == 'csv':
        return pd.read_csv(upload, sep=None, engine='python')
    elif extension in ['xlsx', 'xls']:
        return pd.read_excel(upload)

    return None