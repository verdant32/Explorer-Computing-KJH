import streamlit as st
import pandas as pd
import numpy as np

data = {"요일": ["월", "화", "수", "목", "금"], "강좌수": [3, 2, 3, 0, 1]}
list_data = [["월", 3], ["화", 2], ["수", 3], ["목", 0], ["금", 1]]
df = pd.DataFrame(data)

st.write("### 요일 당 강의 수")
st.table(df)

json_data = {"컴탐": "교수: 변해선, 강의실: 26동 104호"}
st.write("### 수업정보")
st.json(json_data)

st.write("### 이번 학기 요약")
st.metric(label="수강과목수", value="6") 
st.metric(label="총 학점", value="18")




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
