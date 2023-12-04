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


# 假设col2是一个已定义的列
with col2:
    st.title("图片识别结果")
    st.write("")
    st.write("")
    with st.container():
        if st.button("纹路抽取"):
            time.sleep(3.2)
            image_path = 'images/' + '1' + '.png'  # 确保这里的文件扩展名与你的图片匹配
            image = Image.open(image_path)
            st.image(image)

    with st.container():
        if st.button("纹样判断"):
            time.sleep(2)
            # 输出结果，用换行符分隔
            result = "四瓣朵花纹\n八瓣朵花纹\n米字朵花纹\n四合如意纹"
            st.write(result)

    with st.container():
        if st.button("预测结果"):
            time.sleep(1.7)
            st.title("成功")

