import numpy as np
import pandas as pd
import streamlit as st

st.title("DEMO PAGE")
st.write("1234567890")
st.write("# 1")
st.write("## 12")
st.write("### 123")
st.write("#### 1234")

arr1= np.array([1, 2, 3, 4, 5])
st.write(arr1)

df1= pd.DataFrame([[11,22,33,44],[50,60,70,80]],columns=['A', 'B', 'C', 'D'])
st.write(df1)
st.table(df1)

st.write("## 核取方塊")
r1= st.checkbox("外帶")
if r1:
    st.info("外帶已選取")
else:
    st.info("內用")

checks=st.columns(3)
txt=''  
with checks[0]:
    r11=st.checkbox("選項1")
    if r11:
        txt += "選項1已選取\n"
with checks[1]:
    r12=st.checkbox("選項2")
    if r12:
        txt += "選項2已選取\n"
with checks[2]:
    r13=st.checkbox("選項3")
    if r13:
        txt += "選項3已選取\n"
st.info(txt)

st.write("## 單選按鈕")
r2= st.radio("選擇一個", ["咖啡", "果汁", "奶茶"])
st.info(f"你選擇了: {r2}")



st.write("## 單選按鈕")
r3= st.radio("選擇一個", ["咖啡", "果汁", "奶茶"],key="radio2")
st.info(f"你選擇了: {r3}")

st.write("## 滑桿")
num= st.slider("選擇一個數字", 1, 100, 50)
st.info(f"你選擇的數字是: {num}")

st.sidebar.write("## 下拉選單")
city = st.sidebar.selectbox("居住地", ["台北", "台南", "其他"])
if city == "台北":
    st.sidebar.info("你選擇了台北")
elif city == "台南":
    st.sidebar.info("你選擇了台南")
else:
    st.sidebarinfo("你選擇了其他")

st.write("## 按鈕")
a=st.number_input("num...")
b=st.number_input("num2...")
if st.button("相加"):
    st.info(f"### 結果是: {a + b}")