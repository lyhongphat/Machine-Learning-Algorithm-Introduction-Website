import streamlit as st


def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Support vector machine""")

    # lyThuyet ,tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Ví dụ 6", "Ví dụ 7"])
    tab_titles = ["Các khái niệm", "Ví dụ 1", "Ví dụ 1a", "Ví dụ 2", "Plot LinearSVC Support Vector", ]
    tabs = st.tabs(tab_titles)
    with tabs[0]:
        import bruh.SVM.Theory
        bruh.SVM.Theory.executeThisFunction()

    with tabs[1]:
        st.title("Ví dụ minh họa")
        import bruh.SVM.Bai01
        bruh.SVM.Bai01.executeThisFunction()

    with tabs[2]:
        st.title("Ví dụ minh họa")
        import bruh.SVM.Bai01a
        bruh.SVM.Bai01a.executeThisFunction()

    with tabs[3]:
        import bruh.SVM.Bai02
        st.title("Ví dụ minh họa")
        bruh.SVM.Bai02.executeThisFunction()

    with tabs[4]:
        st.title("Ví dụ minh họa")
        import bruh.SVM.plot_linearsvc_support_vectors
        bruh.SVM.plot_linearsvc_support_vectors.executeThisFunction()
