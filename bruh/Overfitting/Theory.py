import streamlit as st


def display():
    st.title("""Các khái niệm""")

    st.markdown \
        ("""
        Overfitting không phải là một thuật toán trong Machine Learning. Nó là một hiện tượng không mong muốn thường gặp, người xây dựng mô hình Machine Learning cần nắm được các kỹ thuật để tránh hiện tượng này.

# ****Giới thiệu****

Trong các bài toán ***supervised learning***, chúng ta thường phải đi tìm một mô hình ánh xạ các vector đặc trưng thành các kết quả tương ứng trong training set. Tức là đi tìm hàm số  $f$ sao cho $y_i ≈ f(x_i), ∀i = 1, 2, . . . , N$. Một cách tự nhiên, ta sẽ đi tìm các tham số mô hình của $f$ sao cho việc xấp xỉ có sai số càng nhỏ càng tốt. Nói cách khác, mô hình càng khớp *(fit)* với dữ liệu càng tốt. Tuy nhiên, sự thật là nếu một mô hình quá fit với dữ liệu thì nó sẽ gây phản tác dụng. Hiện tượng quá ***fit*** này trong machine learning được gọi là ***overfitting***.
Đây là một hiện tượng xấu cần tránh. Vì có thể mô hình rất fit với training set nhưng lại không biểu diễn tốt dữ liệu không được nhìn thấy khi huấn luyện. Một mô hình chỉ mô tả tốt training set là mô hình không có tính tổng quát (*generalization*). Một mô hình tốt là mô hình có tính tổng quát.
Để có cái nhìn đầu tiên về *overfitting*, chúng ta cùng xem ví dụ bên dưới. Có 50 điểm dữ liệu, ở đó đầu ra bằng một đa thức bậc ba của đầu vào cộng thêm nhiễu. Tập dữ liệu này được chia làm hai phần: 30 điểm dữ liệu màu đỏ là training set, 20 điểm dữ liệu màu vàng là dữ liệu kiểm thử. Đồ thị của đa thức bậc ba này được cho bởi đường nét đứt màu xanh lục. Bài toán đặt ra là giả sử ta không biết mô hình ban đầu mà chỉ biết các điểm dữ liệu, hãy tìm một mô hình tốt để mô tả quan hệ giữa đầu vào và đầu ra của dữ liệu đã cho. Giả sử biết thêm rằng mô hình được mô tả bởi một đa thức. Nhắc lại đa thức nội suy Lagrange. Cho $N$ cặp điểm dữ liệu $(x_1, y_1), (x_2, y_2), . . . ,(x_N , y_N )$ với các xi khác nhau đôi một, luôn tìm được một đa thức $P(.)$ bậc không vượt quá  $N − 1$ sao cho $P(x_i) = y_i, ∀i = 1, 2, . . . , N.$
        """)

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

    st.markdown("""Như đã đề, với loại dữ liệu này, chúng ta có thể áp dụng ***polynomial regression*** với vector đặc trưng là $x = [1, x, x_2, x_3, . . . , xd]^T$ cho đa thức bậc $d$. Điều quan trọng là cần xác định bậc d của đa thức. Rõ ràng là một đa thức bậc không vượt quá 29 có thể fit được hoàn toàn với 30 điểm trong
tập training set. Xét một vài giá trị $d = 2, 4, 8, 16$. Với d = 2, mô hình không thực sự tốt vì mô hình dự đoán *(predicted model)* quá khác so với mô hình thực *(true model)*; thậm chí nó có xu hướng đi xuống khi mà dữ liệu đang có hướng đi lên. Trong trường hợp này, ta nói mô hình bị *underfitting*. Với $d = 8$, với các điểm dữ liệu trong training set, mô hình dự đoán và mô hình thực là khá giống nhau. Tuy nhiên, về phía phải, đa thức bậc 8 cho kết quả hoàn toàn ngược với xu hướng của dữ liệu. Điều tương tự xảy ra trong trường hợp $d = 16$. Đa thức bậc 16 này quá fit training set. Việc quá fit trong trường hợp bậc 16 là không tốt vì mô hình có thể đang cố gắng mô tả nhiễu hơn là dữ liệu. Hiện tượng xảy ra ở hai trường hợp đa thức bậc cao này được gọi là *overfitting*. Độ phức tạp của đồ thị trong hai trường hợp này cũng khá lớn, dẫn đến các đường dự đoán không được tự nhiên.

Với $d = 4$, mô hình dự đoán khá giống với mô hình thực. Hệ số bậc cao nhất tìm được rất gần với $0^1$, vì vậy đa thưc bậc bốn này khá gần với đa thức bậc ba ban đầu. Đây chính là một mô hình tốt.
***Overfitting*** là hiện tượng mô hình tìm được quá khớp với dữ liệu huấn luyện. Việc này sẽ gây ra hậu quả lớn nếu trong training set có nhiễu. Khi đó, mô hình quá chú trọng vào việc xấp xỉ training set mà quên đi việc quan trọng hơn là tính tổng quát, khiến cho mô hình không thực sự mô tả tốt dữ liệu ngoài training set. Overfitting đặc biệt xảy ra khi lượng dữ liệu huấn luyện quá nhỏ hoặc độ phức tạp của mô hình quá cao. Trong ví dụ trên đây, độ phức tạp của mô hình có thể được coi là bậc của đa thức cần tìm.
***Vậy, có những kỹ thuật nào giúp tránh overfitting?***
Trước hết, chúng ta cần một vài đại lượng để đánh giá chất lượng của mô hình trên training
set và test set. Dưới đây là hai đại lượng đơn giản, với giả sử $y$ là đầu ra thực sự (có thể là
vector), và $\overline{y}$ là đầu ra dự đoán bởi mô hình.
***Training error:*** Đại lượng này là mức độ sai khác giữa đầu ra thực và đầu ra dự đoán của
mô hình, thường là giá trị của hàm mất mát áp dụng lên training data. Hàm mất mát này
cần có một thừa số $\\frac{1}{Ntrain}$ để tính giá trị trung bình, tức mất mát trung bình trên mỗi điểm dữ liệu. Với các bài toán regression, đại lượng này thường được xác định bởi ***mean squared error*** (MSE).""")

    st.image("bruh/assets/images/overfitting/theory/1.png")

    st.markdown("""Với ***classification***, trung bình cộng của cross entropy loss (với softmax regression) hoặc hinge loss (với multi-class SVM) thường được sử dụng.
***Test error***: Tương tự như trên, nhưng mô hình tìm được được áp dụng vào test data. Chú ý rằng, khi xây dựng mô hình, ta không được sử dụng thông tin trong tập dữ liệu này. Với regression, đại lượng này thường được định nghĩa bởi""")

    st.image("bruh/assets/images/overfitting/theory/2.png")
    st.markdown("""Việc lấy trung bình là quan trọng vì lượng dữ liệu trong tập huấn luyện và tập kiểm thử có
thể chênh lệch rất nhiều.
Một mô hình được coi là tốt (fit) nếu cả training error và test error đều thấp. Nếu training
error thấp nhưng test error cao, ta nói mô hình bị overfitting. Nếu training error cao và
test error cao, ta nói mô hình bị underfitting. Xác suất để xảy ra việc training error cao
nhưng test error thấp là rất nhỏ.""")