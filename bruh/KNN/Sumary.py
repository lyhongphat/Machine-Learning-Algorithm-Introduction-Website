import streamlit as st


def display():
    tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Lý thuyết",
        "Ví dụ 1",
        "Ví dụ 2",
        "Ví dụ 3",
        "Ví dụ 4",
        "Ví dụ 5",
        "Ví dụ 6",
    ])

    with tab0:
        import bruh.KNN.Theory as theory
        theory.display()