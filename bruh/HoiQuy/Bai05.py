from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def display():
    displayDemo()
    displayDes()

def displayDemo():
    st.markdown\
        ("""
        ## Khử nhiễu bằng cách dùng HuberRegressor

```python
# height (cm), input Data, each row is a Data point
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([49, 50, 90, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

huber_reg = linear_model.HuberRegressor()
huber_reg.fit(X, y)  # in scikit-learn, each sample is one row
# Compare two results
print("scikit-learn’s solution : w_1 = ", huber_reg.coef_[0], "w_0 = ", huber_reg.intercept_)

X = X[:, 0]

fig, ax = plt.subplots()
ax.plot(X, y, 'ro')

a = huber_reg.coef_[0]
b = huber_reg.intercept_
x1 = X[0]
y1 = a * x1 + b
x2 = X[12]
y2 = a * x2 + b
x = [x1, x2]
y = [y1, y2]

ax.plot(x, y)
st.pyplot(fig)
```
        """)
    # height (cm), input Data, each row is a Data point
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
    y = np.array([49, 50, 90, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

    huber_reg = linear_model.HuberRegressor()
    huber_reg.fit(X, y)  # in scikit-learn, each sample is one row
    # Compare two results
    print("scikit-learn’s solution : w_1 = ", huber_reg.coef_[0], "w_0 = ", huber_reg.intercept_)

    X = X[:, 0]

    fig, ax = plt.subplots()
    ax.plot(X, y, 'ro')

    a = huber_reg.coef_[0]
    b = huber_reg.intercept_
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
    st.markdown \
        ("""
        ## Ridge regression

Trong trường hợp ma trận $XX^T$ không khả nghịch, có một kỹ thuật nhỏ để tránh hiện tượng này là biến đổi $XX^T$ một chút để biến nó trở thành $A = XX^T + λI$ với $λ$  là một số dương rất nhỏ và $I$ là ma trận đơn vị với bậc phù hợp.

Ma trận $A$  là khả nghịch vì nó là một ma trận xác định dương. Thật vậy, với mọi $w ≠ 0$
        """)

    st.image("bruh/assets/images/HoiQuy/51.png")
    st.markdown\
        ("""
        Lúc này, nghiệm của bài toán là $y = (XX^T + λI)^{-1} Xy$. Nếu xét hàm mất mát
    """)
    st.image("bruh/assets/images/HoiQuy/52.png")
    st.markdown\
        ("""
        với phương trình đạo hàm theo $w$  bằng không:
    """)
    st.image("bruh/assets/images/HoiQuy/53.png")
    st.markdown\
        ("""
        Ta thấy $w = (XX^T +λI)^{−1}Xy$ chính là nghiệm của bài toán tối thiểu $L2(w)$. Mô hình machine learning với hàm mất mát còn được gọi là *ridge regression.*

## Phương pháp tối ưu khác

Linear regression là một mô hình đơn giản, lời giải cho phương trình đạo hàm bằng không cũng khá đơn giản. Trong hầu hết các trường hợp, chúng ta không thể giải được phương trình đạo hàm bằng không. Tuy nhiên, nếu một hàm mất mát có đạo hàm không quá phức tạp, nó có thể được giải bằng một phương pháp rất hữu dụng có tên là **gradient descent**. Trên thực tế, một vector đặc trưng có thể có kích thước rất lớn, dẫn đến ma trận XX^T cũng có kích thước lớn và việc tính ma trận nghịch đảo có thể không lợi về mặt tính toán. **Gradient descent** sẽ giúp tránh được việc tính ma trận nghịch đảo.
        """)