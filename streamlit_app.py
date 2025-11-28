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
