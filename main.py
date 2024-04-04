import streamlit as st

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