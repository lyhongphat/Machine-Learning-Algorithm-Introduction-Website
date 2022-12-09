import streamlit as st

def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Giảm dần đạo hàm""")

    # lyThuyet ,tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Ví dụ 6", "Ví dụ 7"])
    tab_titles = ["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 2a", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Temp"]
    tabs = st.tabs(tab_titles)
    with tabs[0]:
        import bruh.GiamDanDaoHam.Theory
        bruh.GiamDanDaoHam.Theory.executeThisFunction()

    with tabs[1]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.Bai01
        bruh.GiamDanDaoHam.Bai01.executeThisFunction()

    with tabs[2]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.Bai02
        bruh.GiamDanDaoHam.Bai02.executeThisFunction()

    with tabs[3]:
        import bruh.GiamDanDaoHam.Bai02a
        st.title("Ví dụ minh họa")
        bruh.GiamDanDaoHam.Bai02a.executeThisFunction()

    with tabs[4]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.Bai03
        bruh.GiamDanDaoHam.Bai03.executeThisFunction()

    with tabs[5]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.Bai04
        bruh.GiamDanDaoHam.Bai04.executeThisFunction()

    with tabs[6]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.Bai05
        bruh.GiamDanDaoHam.Bai05.executeThisFunction()

    with tabs[7]:
        st.title("Ví dụ minh họa")
        import bruh.GiamDanDaoHam.temp
        bruh.GiamDanDaoHam.temp.executeThisFunction()
