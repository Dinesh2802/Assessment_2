import streamlit as st

# Setting up the page config
st.set_page_config(page_icon="📖", page_title="BookScape Explorer", layout="centered")

# Welcome message
st.title(''':green[***Welcome to BookScape Explorer***]''')


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://pixabay.com/get/g04dd5bea6482de26076a50dabb3c297b7ba29c30505e7bcc7c464fc8460e00fb59579e617d9a322c8b0fbb1dee26db50d54853bbc3a717dc58c9012876d2cf7f_1280.jpg");
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
