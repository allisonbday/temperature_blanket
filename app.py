# IMPORTS ---------------------------------------------------------------------
import os
import streamlit as st
from PIL import Image

# PAGE SET UP -----------------------------------------------------------------
path = os.path.dirname(__file__)

st.set_page_config(
    page_icon="🧶", page_title="Temperature Blanket Generator"
)  # , layout="wide")

image = Image.open(path + "\\static\\images\\yarn.png")
st.image(
    image,
    width=100,
)

st.title("Temperature Blanket Calculator")
