import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/dash.jpeg")

with col2:
    st.title("Dash Presents")
    content = """
    Hello! I'm Dash, a creative and technically adept game designer, proficient Python programmer,
    and passionate ethical hacker. With a unique blend of artistic vision and technical prowess, 
    I specialize in crafting immersive game experiences, developing innovative software solutions, 
    and ensuring the security and integrity of digital environments."""
    st.info(content)

    content2 = """Discover the applications I've crafted below, each a testament to my journey
     in blending creativity with technology to solve, entertain, and innovate.  Hello! I'm Dash, 
     a creative and technically adept game designer, proficient Python programmer,
    and passionate ethical hacker. With a unique blend of artistic vision and technical prowess, 
    I specialize in crafting immersive game experiences, developing innovative software solutions, 
    and ensuring the security and integrity of digital environments"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])