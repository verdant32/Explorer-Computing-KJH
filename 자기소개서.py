
import streamlit as st
import pandas as pd





# write()함수는 다목적 함수로 텍스트, 마크다운, 데이터, 객체 등 다양한 요소를 자동으로 감지하여 인식함
st.write("# 자기소개서") 
st.write("Hello, Streamlit!")
st.write("**국어국문학과 25학번**입니다.")
st.write(303)                        # 숫자
st.write({"이름": "김주희", "나이": 20})   # 딕셔너리
st.write(pd.DataFrame({"A": [1,2,3]})) # 데이터프레임


st.header("좋아하는 음식")
st.caption("달달한 간식을 좋아합니다.")
st.code("print('Nice to meet you!')", language="python")
