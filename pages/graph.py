import streamlit as st
import streamlit.components.v1 as components

st.title('Literary Network')

HtmlFile = open("data/events2014.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 1200, width=1000)