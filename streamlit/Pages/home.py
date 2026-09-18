import streamlit as st

st.title("MC Match")
st.write("This page will match you with your next MC with our machine learned model!")
st.write("There is also a feature for valuating your current MC.")

col1, divider, col2 = st.columns([1, 0.05, 1])

st.markdown("""
    <style>
    /* Visa divider på större skärmar */
    .divider {
        border-left: 2px solid #ccc;
        height: 300px;
        margin: auto;
    }

    /* Dölj divider på mindre skärmar */
    @media (max-width: 768px) {
        .divider {
            display: none;
        }
    }
    </style>
""", unsafe_allow_html=True)


with col2:
    st.markdown(
        """
        ### Match

        This is our classification model that will estimate
        what type of MC matches you.
        You will enter some variables that will get sent
        to our Random Forest classifier model.
        """
    )

    button_left, button, button_right = st.columns([1, 2, 1])

    with button:
        if st.button("Match", use_container_width=True):
            st.switch_page("pages/match.py")


with divider:
    st.markdown(
        """
        <div class="divider"></div>
        """,
        unsafe_allow_html=True
    )


with col1:
    st.markdown(
        """
        ### Valuation

        This is our valuation model. You will enter some
        variables about your MC and get an estimated value.
        """
    )

    button_left, button, button_right = st.columns([1, 2, 1])

    with button:
        if st.button("Valuation", use_container_width=True):
            st.switch_page("pages/valuation.py")