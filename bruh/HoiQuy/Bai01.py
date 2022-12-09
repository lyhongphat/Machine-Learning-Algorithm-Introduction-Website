import numpy as np
import streamlit as st

def display():
    st.header("Ví dụ: Đoán cân nặng thông qua chiều cao")
    displayDemo()
    st.header("Giải thích")
    displayDes()


def displayDes():
    st.markdown \
        ("""
                ## Mô tả
        Ta có tập dữ liệu mẫu tương quan giữa chiều cao và cân nặng như sau:

        | Chiều cao | 147 | 150 | 153 | 158 | 163 | 165 | 168 | 170 | 173 | 175 | 178 | 180 | 183 |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        | Cân nặng | 49 | 50 | 51 | 54 | 58 | 59 | 60 | 62 | 63 | 64 | 66 | 67 | 68 |
                """)

    st.code \
        ("""
        import numpy as np

# height (cm), input Data, each row is a Data point
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]])
one = np.ones((1, X.shape[1]))
Xbar = np.concatenate((one, X), axis=0)  # each point is one row
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
A = np.dot(Xbar, Xbar.T)
b = np.dot(Xbar, y)
w = np.dot(np.linalg.pinv(A), b)
# weights
w_0, w_1 = w[0], w[1]
        """)


def displayDemo():
    # height (cm), input Data, each row is a Data point
    # X là ma trận chiều cao
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]])

    # Tạo chuỗi các phần tử = 1 với kích thước bằng với shape của X
    one = np.ones((1, X.shape[1]))

    # Nối chuỗi one với chuỗi X theo chiều dọc
    Xbar = np.concatenate((one, X), axis=0)  # each point is one row

    # y là ma trận cân nặng, theo chiều chuyển vị với X
    y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

    # Tích vô hướng Xbar với Xbar chuyển vị
    A = np.dot(Xbar, Xbar.T)

    # Tích vô hướng Xbar với y chuyển vị
    b = np.dot(Xbar, y)

    w = np.dot(np.linalg.pinv(A), b)

    # weights
    w_0, w_1 = w[0], w[1]

    x_input = 0
    x_input = st.number_input("Nhập chiều cao để dự đoán cân nặng: ")

    if (x_input < 100):
        st.warning("Chiều cao phải lớn hơn 100")
    else:
        y_output = w_1 * x_input + w_0
        st.success("Với chiều cao vừa nhập, cân nặng được dự đoán là %.2fkg" % y_output)
