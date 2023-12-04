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


with col2:
    st.title("图片识别结果")
    st.write("")
    st.write("")
    with st.container():
        if st.button("纹路抽取"):
            time.sleep(3.2)
            
            # 显示四种不同的纹路图片
            image_names = ['四瓣朵花纹', '八瓣朵花纹', '米字朵花纹', '四合如意纹']
            for name in image_names:
                image_path = 'images/' + name
                image = Image.open(image_path)
                st.image(image)

    with st.container():
        if st.button("纹样判断"):
            time.sleep(2)
            # 这里需要你的逻辑来决定显示哪个纹样名称
            # 例如，你可以根据用户的选择或某些条件来设置 new_filename
            # 下面是一个示例：
            new_filename = "四瓣朵花纹、八瓣朵花纹、米字朵花纹、四合如意纹"
            st.title(new_filename)

    with st.container():
        if st.button("预测结果"):
            time.sleep(1.7)
            st.title("成功")
