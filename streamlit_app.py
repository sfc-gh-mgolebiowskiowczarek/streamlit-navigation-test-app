import streamlit as st

pages = {
    "Section 1": [
        st.Page("page_1.py", title="Page 1"),
        st.Page("page_2.py", title="Page 2"),
    ],
    "Section 2": [
        st.Page("page_3.py", title="Page 3"),
        st.Page("page_4.py", title="Page 4"),
    ],
}

pg = st.navigation(pages)
pg.run()
