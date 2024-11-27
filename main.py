# streamlit에 쓸 파일
# ml은 colab
import streamlit as st
from page1 import page1


pg = st.navigation([
    st.Page(page1, title="Stock 데이터분석", icon=":material/favorite:"),
    st.Page("page2.py", title="캘리포니아 집값 예측", icon="🔥"),
])
pg.run()