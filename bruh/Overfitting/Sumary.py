import streamlit as st


def display():
    st.title("Overfitting")
    tab1, tab2, tab3 = st.tabs(["Overfitting là gì", "Ví dụ", "Cách tránh Overfitting"])
    with tab1:
        import bruh.Overfitting.Theory
        bruh.Overfitting.Theory.display()
    with tab2:
        st.title("Ví dụ")
        option = st.selectbox("Chọn bậc của đa thức", [2, 4, 8, 16])
        if option == 2:
            import bruh.Overfitting.Bai01a
            bruh.Overfitting.Bai01a.display()
        elif option == 4:
            import bruh.Overfitting.Bai01b
            bruh.Overfitting.Bai01b.display()
        elif option == 8:
            import bruh.Overfitting.Bai01c
            bruh.Overfitting.Bai01c.display()
        elif option == 16:
            import bruh.Overfitting.Bai01d
            bruh.Overfitting.Bai01d.display()

    with tab3:
        import bruh.Overfitting.avoidOverfitting as avOf
        avOf.display()
