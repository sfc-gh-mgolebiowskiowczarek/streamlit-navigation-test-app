import streamlit as st

st.text('Page 1')

st.header('st.button')

if st.button('Say hello'):
    st.write('Hello there!')
else:
    st.write('Goodbye!')
