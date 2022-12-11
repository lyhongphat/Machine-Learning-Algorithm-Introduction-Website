import streamlit as st


def display():
    st.title("Overfitting")
    tab1, tab2 = st.tabs(["Overfitting là gì", "Cách tránh Overfitting"])
    with tab1:
        import bruh.Overfitting.Theory
        bruh.Overfitting.Theory.display()

    with tab2:
        import bruh.Overfitting.avoidOverfitting as avOf
        avOf.display()
