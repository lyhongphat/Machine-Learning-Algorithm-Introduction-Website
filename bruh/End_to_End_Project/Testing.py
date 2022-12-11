import streamlit as st

def display():
    st.title("Testing")

    algo2 = st.selectbox \
        ("Chọn thuật toán để Testing",
         [
             "Linear Regression",
             "Decision tree Regression",
             "Random forest Regression",
             "Random forest Regression - Grid search",
             "Random forest Regression - Random search"
         ])

    st.button(label="Testing", on_click=testingClick(algo2))
    st.header("Code: ")


def testingClick(algorithm):
    if algorithm == "Linear Regression":
        import bruh.End_to_End_Project.CaliHousing.Test.Linear_Regression_UseModel as test
        with st.spinner("Đang tải model..."):
            test.testing()
        st.success("Đã xong")
    elif algorithm == "Decision tree Regression":
        import bruh.End_to_End_Project.CaliHousing.Test.Decision_Tree_Regression_UseModel as test
        with st.spinner("Đang tải model..."):
            test.testing()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression":
        import bruh.End_to_End_Project.CaliHousing.Test.Random_Forest_Regression_UseModel as test
        with st.spinner("Đang tải model..."):
            test.testing()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression - Grid search":
        import bruh.End_to_End_Project.CaliHousing.Test.Random_Forest_Regression_Grid_Search_CV_UseModel as test
        with st.spinner("Đang tải model..."):
            test.testing()
        st.success("Đã xong")
    elif algorithm == "Random forest Regression - Random search":
        import bruh.End_to_End_Project.CaliHousing.Test.Random_Forest_Regression_Random_Search_CV_UseModel as test
        with st.spinner("Đang tải model..."):
            test.testing()
        st.success("Đã xong")

