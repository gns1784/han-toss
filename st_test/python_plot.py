# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly 
import numpy as np 
import matplotlib as mpl

@st.cache_data
def get_data():
    # data = pd.read_csv("train.csv") / size가 크면 streamlit에서 배포 안됨
    data = sns.load_dataset("tips")
    return data

def main():
    price = st.slider("단가:", 1000, 10000, value = 5000)
    total_sales = st.slider("전체 판매 갯수:", 1, 1000, value = 500) 

    if st.button("매출액 계산"):
        revenue = price * total_sales
        st.write(f"전체매출액 : {revenue}")

    tips = get_data()

    show_plot = st.checkbox("시각화를 보여줄까요?")

    tip_max = tips['tip'].max() # tip의 최대
    tip_min = tips['tip'].min()
    tip = st.slider("tip의 입력값", tip_min, tip_max)
    tip2 = tips.loc[tips['tip'] >= tip, :] # 조건
    Thur = tips[tips['day']=='Thur']
    Sun = tips[tips['day']=='Sun']
    Sat = tips[tips['day']=='Sat']
    Fri = tips[tips['day']=='Fri']
    option = st.selectbox(
        "요일을 선택하세요",
        ("Thur", "Sun", "Sat", "Fri")
    )


    import plotly.express as px
    fig = px.scatter(data_frame = tip2, x="total_bill", y="tip") # 조건에 맞는 데이터프레임 시각화
    st.plotly_chart(fig)

    if show_plot:

        fig, ax = plt.subplots()
        ax.set_title("Hello World")
        st.pyplot(fig)
    




if __name__ == "__main__":
    main()