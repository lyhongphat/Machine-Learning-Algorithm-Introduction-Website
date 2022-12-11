from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def display():
    displayDemo()
    displayDes()

def displayDemo():
    # height (cm), input Data, each row is a Data point
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
    y = np.array([49, 50, 90, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

    regr = linear_model.LinearRegression()
    regr.fit(X, y)  # in scikit-learn, each sample is one row
    # Compare two results
    print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)

    X = X[:, 0]

    fig, ax = plt.subplots()
    ax.plot(X, y, 'ro')

    a = regr.coef_[0]
    b = regr.intercept_
    x1 = X[0]
    y1 = a * x1 + b
    x2 = X[12]
    y2 = a * x2 + b
    x = [x1, x2]
    y = [y1, y2]

    ax.plot(x, y)
    st.pyplot(fig)

def displayDes():
    st.header("Giải thích")
    st.markdown\
        ("""
        Hạn chế đầu tiên của linear regression là nó rất **nhạy cảm với nhiễu** (sensitive to noise).

Trong ví dụ về mối quan hệ giữa chiều cao và cân nặng bên trên, nếu có chỉ một cặp dữ liệu nhiễu (150 cm, 90kg) thì kết quả sẽ sai khác đi rất nhiều.
Vì vậy, trước khi thực hiện linear regression, các nhiễu cần phải được loại bỏ. Bước này được gọi là tiền xử lý (pre-processing). Hoặc hàm mất mát có thể thay đổi một chút để tránh việc tối ưu các nhiễu bằng cách sử dụng Huber loss. Linear regression với Huber loss được gọi là Huber regression, được khẳng định là robust to noise (ít bị ảnh hưởng hơn bởi nhiễu). Xem thêm Huber Regressor, scikit learn.
Hạn chế thứ hai của linear regression là nó không biễu diễn được các mô hình phức tạp. Mặc dù trong phần trên, chúng ta thấy rằng phương pháp này có thể được áp dụng nếu quan hệ giữa outcome và input không nhất thiết phải là tuyến tính, nhưng mối quan hệ này vẫn đơn giản nhiều so với các mô hình thực tế. Hơn nữa, việc tìm ra các đặc trưng $x^2_1, sin(x_2), x_1x_2$ như ở trên là ít khả thi.
        """)