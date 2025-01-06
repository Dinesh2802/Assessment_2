import streamlit as st

# Setting up the page config
st.set_page_config(page_icon="📖", page_title="BookScape Explorer", layout="centered")

# Welcome message
st.title(''':green[***Welcome to BookScape Explorer***]''')


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://getwallpapers.com/wallpaper/full/1/b/a/166020.jpg");
background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}   

[data-testid="stSidebarContent"]{
background-color: rgba(0, 0, 0, 0);
background-size: cover;
}
</style>
"""

# Display the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Home page content
st.sidebar.markdown("🏠[Home](Home)")

# Content for books page
st.sidebar.markdown("📚[Books](Books)")

# Google Search Link
st.sidebar.markdown("🌎[Google](http://www.google.com)")
