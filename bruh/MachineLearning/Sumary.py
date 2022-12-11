import streamlit as st

def display():
    st.title("Machine Learning")
    st.markdown("""# Môn học: Học máy

Mã lớp: [MALE431984_22_1_04](https://utex.hcmute.edu.vn/course/view.php?id=25258)

# Giảng viên hướng dẫn:

Giảng viên hướng dẫn: Ts. Trần Tiến Đức

# Nhóm thực hiện:

**Danh sách thành viên nhóm thực hiện:** 

Võ Văn Đức - 20110635

Lý Hồng Phát - 20110692

Nguyễn Thanh Trung - 20110755

***Link file rar báo cáo:***

`https://drive.google.com/file/d/1ZGLmfOEsIdOKVzdsNTN7Ccdzo22rOHl2/view?usp=sharing`

***Link web:***

`https://khowfsix-finalproject-machinelearning-main-8p3ort.streamlit.app/`

# Giới thiệu môn học

**AI - Trí tuệ nhân tạo** (*Artificial Intelligence*) là các kỹ thuật giúp cho máy tính thực hiện được những công việc của con người chúng ta. Ví dụ như một chương trình cờ vua tự động có thể coi là một chương trình có sử dụng AI hay viết tắt là một chương trình AI.

Trong lĩnh vực AI có một nhánh nghiên cứu về khả năng tự học của máy tính được gọi là **học máy** (*machine learning*). Hiện nay không có 1 định nghĩa chính thức nào về học máy cả nhưng có thể hiểu rằng nó là các kỹ thuật giúp cho máy tính có thể tự học mà không cần phải cài đặt các luật quyết định. Thường một chương trình máy tính cần các quy tắc, luật lệ để có thể thực thi được một tác vụ nào đó như dán nhãn cho các email là thư rác nếu nội dung email có chứ từ khoá “quảng cáo”. Nhưng với học máy, các máy tính có thể tự động phân lại các thư rác thành mà không cần chỉ trước bất kỳ quy tắc nào cả. Nói hơi khó thoát ý, nhưng có thể hiểu đơn giản là nó giúp cho máy tính có được cảm quan và suy nghĩ được như con người. Còn nếu nói nôm na kỹ thuật một chút thì học máy là phương pháp vẽ các đường thể hiện mối quan hệ của tập dữ liệu. Ví dụ như đường ngăn cách 2 loại dữ liệu cho nhãn khác nhau, đường thể hiện xu hướng của giá nhà phụ thuộc vào diện tích và trí hay các đường phân cụm dữ liệu.

Một nhánh nhỏ trong học máy gần đây rất được ưu chuộng là **học sâu** (*deep learning*). Học sâu là kỹ thuật sử dụng các mạng nơ-ron tương tự như các nơ-ron của não người để xây dựng hệ thống học máy. Đây là một sự kết hợp tuyệt vời giữa toán học và khoa học thần kinh. Kết quả của nó mang lại cực kỳ to lớn, có thể coi là khởi nguyên của ngành công nghiệp mới. Tại thời điểm này, hầu hết các anh lớn cả trong ngành công nghệ lẫn các ngành khác như ôto, điện tử đều đang tập trung phát triển và ứng dụng kỹ thuật học sâu cho bài toán của mình. Ví dụ như [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo) của Google đã chiến thắng nhà vô địch cờ vây Lee Sedol vào tháng 3 năm 2016. Tính năng nhận diện khuôn mặt khá chính xác của Facebook được triển khai vào năm 2016. Trợ lý ảo Siri của Apple được giới thiệu từ năm 2006. Xe tự lái của Google được thử nghiệm chính thức trên đường phố vào năm 2015,…

# ****Phân loại kỹ thuật học máy****

Các giải thuật học máy được phân ra làm 2 loại chính là:

- **Học có giám sát** (*Supervised Learning*): Là phương pháp sử dụng những dữ liệu đã được gán nhãn từ trước để suy luận ra quan hệ giữa đầu vào và đầu ra. Các dữ liệu này được gọi là dữ liệu huấn luyện và chúng là cặp các đầu vào-đầu ra. Học có giám sát sẽ xem xét các tập huấn luyện này để từ đó có thể đưa ra dự đoán đầu ra cho 1 đầu vào mới chưa gặp bao giờ. Ví dụ dự đoán giá nhà, phân loại email.
- **Học phi giám sát** (*Unsupervised Learning*): Khác với học có giám sát, học phi giám sát sử dụng những dữ liệu chưa được gán nhãn từ trước để suy luận. Phương pháp này thường được sử dụng để tìm cấu trúc của tập dữ liệu. Tuy nhiên lại không có phương pháp đánh giá được cấu trúc tìm ra được là đúng hay sai. Ví dụ như phân cụm dữ liệu, triết xuất thành phần chính của một chất nào đó.

Ngoài ra còn có 1 loại nữa là **học tăng cường** (*reinforcement learning*). Phương pháp học tăng cường tập trung vào việc làm sao để cho 1 tác tử trong môi trường có thế hành động sao cho lấy được phần thưởng nhiều nhất có thể. Khác với học có giám sát nó không có cặp dữ liệu gán nhãn trước làm đầu vào và cũng không có đánh giá các hành động là đúng hay sai.""")