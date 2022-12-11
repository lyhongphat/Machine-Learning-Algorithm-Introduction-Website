import streamlit as st
import pandas as pd


def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Dự đoán giá nhà Cali Housing""")

    tab1, tab2, tab3, tab4 = st.tabs(["Mô tả", "Dữ liệu", "Training", "Test"])
    with tab1:
        tab1Display()
    with tab2:
        tab2Display()
    with tab3:
        tab3Display()
    with tab4:
        tab4Display()


def tab1Display():
    import bruh.End_to_End_Project.Description as des
    des.display()


def tab2Display():
    st.title("Dữ liệu")
    st.header("Dataframe housing.csv:")

    housing = pd.read_csv("bruh/End_to_End_Project/CaliHousing/Data/housing.csv")
    st.dataframe(housing)


def tab3Display():
    algo = st.selectbox \
        ("Chọn thuật toán để Training",
         [
             "Linear Regression",
             "Decision tree Regression",
             "Random forest Regression",
             "Random forest Regression - Grid search",
             "Random forest Regression - Random search"
         ])

    st.button(label="Training", on_click=trainingClick(algo))
    st.header("Code: ")
    import bruh.End_to_End_Project.Training as tr
    tr.display(algo)


def trainingClick(algorithm):
    # msg = st.warning("Chờ training nè, hơi lâu đấy")

    if algorithm == "Linear Regression":
        import bruh.End_to_End_Project.CaliHousing.Training.Linear_Regression as train
        with st.spinner("Training..."):
            train.training()
        st.success("Đã xong")
    elif algorithm == "Decision tree Regression":
        import bruh.End_to_End_Project.CaliHousing.Training.Decision_Tree_Regression as train
        with st.spinner("Training..."):
            train.training()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression":
        import bruh.End_to_End_Project.CaliHousing.Training.Random_Forest_Regression as train
        with st.spinner("Training..."):
            train.training()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression - Grid search":
        import bruh.End_to_End_Project.CaliHousing.Training.Random_Forest_Regression_Grid_Search_CV as train
        with st.spinner("Training..."):
            train.training()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression - Random search":
        import bruh.End_to_End_Project.CaliHousing.Training.Random_Forest_Regression_Random_Search_CV as train
        with st.spinner("Training..."):
            train.training()
        st.success("Đã xong")

    # msg = st.success("Đã training xong")
    pass


def tab4Display():
    pass
