import streamlit as st
from PIL import Image
import time
import os

extension = '.png'
base_dir='images/'
col1, col2 = st.columns(2)

with col1:
   st.title("图片上传与显示")
   uploaded_file = st.file_uploader("选择一个图片文件", type=["jpg", "jpeg", "png"])
   if uploaded_file is not None:
       img = Image.open(uploaded_file)
       
       st.image(img, caption="上传的图片")

with col2:
    st.title("图片识别结果")
    st.write("")
    st.write("")
    with st.container():
        if st.button("纹路抽取"):
            time.sleep(3.2)
            filename = os.path.splitext(os.path.basename(uploaded_file))[0]
            image_path =base_dir+ filename + extension
            st.image(image_path)

    with st.container():
        if st.button("纹样判断"):
            time.sleep(2)
            filename = os.path.splitext(os.path.basename(uploaded_file))[0]
            filename = filename
            st.write("万字菊花纹")

    with st.container():
        if st.button("预测结果"):
            time.sleep(1.7)
            st.write("成功")





