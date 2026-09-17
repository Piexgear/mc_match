import streamlit as st
from app import match, valuation

st.title("MC Match")
st.write("This page will match you with your next mc with our machine learned model!")
st.write("There is also a feature for valuting your current mc")


col1, divider, col2 = st.columns([1, 0.05, 1])

with col1:
    st.markdown(
        """
        This is our classification model that will estemate what type of mc that matches you.
        you will enter some variables that will get sent to the Random forest classifier model 
        """
    )
    
    if st.button("Valuation"):
        st.switch_page(valuation)

with divider:
    st.markdown(
        """
        <div style="
            border-left: 2px solid #ccc;
            height: 300px;
            margin: auto;
        "></div>
        """,
        unsafe_allow_html=True
    )

with col2:
    if st.button("Match"):
        st.switch_page(match)