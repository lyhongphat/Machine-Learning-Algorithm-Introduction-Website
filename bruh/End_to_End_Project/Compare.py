import streamlit as st

def display():
    st.title("So sánh")
    st.markdown("""
    | Linear Regression | Decision Tree Regression | Random Forest Regression | Random Forest Regression - Grid Search CV | Random Forest Regression - Random Search CV |
| --- | --- | --- | --- | --- |
| Sai số bình phương trung bình - train: | Sai số bình phương trung bình - train: | Sai số bình phương trung bình - train: | Sai số bình phương trung bình - train: | Sai số bình phương trung bình - train: |
| 68628.2 | 0 | 18788.21 | 19314.96 | 18045.35 |
| Sai số bình phương trung bình - cross-validation: | Sai số bình phương trung bình - cross-validation: | Sai số bình phương trung bình - cross-validation: | Sai số bình phương trung bình - cross-validation: | Sai số bình phương trung bình - cross-validation: |
| Phương sai: 69049.70 | Phương sai: 71180.83 | Phương sai: 50309.13 | Phương sai: 49613.51 | Phương sai: 48837.66 |
| Độ lệch chuẩn: 2736.48 | Độ lệch chuẩn: 3334.65 | Độ lệch chuẩn: 1976.83 | Độ lệch chuẩn: 1772.56 | Độ lệch chuẩn: 1884.50 |
| Sai số bình phương trung bình - test: | Sai số bình phương trung bình - test: | Sai số bình phương trung bình - test: | Sai số bình phương trung bình - test: | Sai số bình phương trung bình - test: |
| 66911.98 | 70875.27 | 48372.63 | 47856.64 | 46910.92 |
| Đánh giá | Đánh giá | Đánh giá | Đánh giá | Đánh giá |
| Trung bình | Quá khớp do sai số tập train là 0: Tệ | Tốt | Tốt | Tốt |
    """)