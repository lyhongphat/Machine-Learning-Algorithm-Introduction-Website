import streamlit as st


def display():
    st.title("""Ví dụ minh họa""")
    st.header("""K-nearest neighbor""")
    tab0, tab1, tab2, tab3, tab6 = st.tabs([
        "Lý thuyết",
        "Ví dụ 1",
        "Ví dụ 2",
        "Ví dụ 3",
        "Ví dụ 4",

    ])

    with tab0:
        import bruh.KNN.Theory as theory
        theory.display()
    with tab1:
        import bruh.KNN.Bai01 as Bai01
        Bai01.executeThisFunction()
    with tab2:
        import bruh.KNN.Bai02 as Bai02
        Bai02.executeThisFunction()

    with tab3:
        import bruh.KNN.Bai03 as Bai03
        Bai03.executeThisFunction()
        # st.write("")
    # with tab4:
    #     import bruh.KNN.Bai03a as Bai03a
    #     Bai03a.executeThisFunction()
    #     # st.write("")
    # with tab5:
    #     import bruh.KNN.Bai04 as Bai04
    #     Bai04.executeThisFunction()
    #     # st.write("")
    with tab6:
        import  bruh.KNN.Bai08 as Bai08
        Bai08.executeThisFunction()