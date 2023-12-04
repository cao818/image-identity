import streamlit as st
from PIL import Image
import time
import os

filename = ''
extension_const = '.png'
base_dir = 'images/'
col1, col2 = st.columns(2)

with col1:
    st.title("图片上传与显示")
    uploaded_file = st.file_uploader("选择一个图片文件", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        filename, extension = uploaded_file.name.split('.')
        st.image(img, caption="上传的图片")

        # 在这里定义 new_filename
        new_filename = filename[6:]

with col2:
    st.title("图片识别结果")
    st.write("")
    st.write("")
    with st.container():
        if st.button("纹路抽取"):
            time.sleep(3.2)
            
            # 使用 new_filename
            image_path = 'images/' + new_filename + extension_const
            image = Image.open(image_path)
            st.image(image)

    with st.container():
        if st.button("纹样判断"):
            time.sleep(2)
            # 检查 new_filename 是否被定义
            if 'new_filename' in locals():
                st.title(new_filename)

    with st.container():
        if st.button("预测结果"):
            time.sleep(1.7)
            st.title("成功")
