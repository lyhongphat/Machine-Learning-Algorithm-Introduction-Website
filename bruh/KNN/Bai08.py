# import tkinter as tk
# from PIL import ImageTk, Image
# from PIL import  Image
from PIL import Image
import os
import streamlit as st

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
#         self.resizable(True, True)
#         self.image = Image.open('castle.jpg')
#         self.canvas = tk.Canvas(self, relief=tk.SUNKEN, borderwidth=0, bg='white', highlightthickness=0)
#         self.canvas.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
#         self.canvas.bind("<Configure>", self.configure)
#
#     def configure(self, event):
#         self.canvas.delete('all')
#         self.canvas.update()
#         W = self.canvas.winfo_width()
#         H = self.canvas.winfo_height()
#         img = self.image.resize((W, H), Image.ANTIALIAS)
#         self.image_tk = ImageTk.PhotoImage(img)
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

def executeThisFunction():
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "../assets/images/KNN/castle.jpg")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)

    code = '''def __init__(self):
        columnconfigure(0, weight=1)
        rowconfigure(0, weight=1)
        resizable(True, True)
        image = Image.open('castle.jpg')
        canvas = tk.Canvas(self, relief=tk.SUNKEN, borderwidth=0, bg='white', highlightthickness=0)
        canvas.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        canvas.bind("<Configure>", self.configure)'''
    st.code(code, language="python")
    st.write("Phương thức columnconfigure() định cấu hình chỉ mục cột của lưới.")
    st.write("Phương thức columnconfigure() định cấu hình chỉ mục hàng của lưới.")
    st.write("Phương thức resizable() được sử dụng để cho phép cửa sổ gốc thay đổi kích thước của nó theo nhu cầu của người dùng")
    st.write("Mở ảnh castle.jpg bằng Image.open")
    st.write("Tiên hành mở ảnh với không đậm đường liền, không highlight")
    st.write("Phương thức grid() cho phép bạn chỉ định vị trí hàng và cột trong danh sách tham số của nó.")


    code = '''def configure(self, event):
        canvas.delete('all')
        canvas.update()
        W = self.canvas.winfo_width()
        H = self.canvas.winfo_height()
        img = self.image.resize((W, H), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)'''
    st.code(code, language = "python")
    st.write("canvas.delete dùng để loại bỏ những dữ liệu chứa trong bộ nhớ tạm của nó")
    st.write("canvas.update tiến hành cập nhật lại những thông tin mới được cung cấp")
    st.write("Tiến hành thiết lập độ dài, rộng cho khung tranh")
    st.write("tiến hành sử dụng phương thức resize() để đặt lại kích thước ảnh")





    # image = Image.open('castle.jpg')
    # st.image(image, caption='Output', use_column_width=True)

if __name__ == "__main__":
    executeThisFunction()

