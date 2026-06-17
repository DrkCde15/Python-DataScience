import streamlit as st

pg = st.navigation(
    [st.Page('./pages/home.py',),
     st.Page('./pages/page2.py'),
     st.Page('./pages/page3.py'),
     ],
    position='top'
)
pg.run()