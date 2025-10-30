import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"  # "맑은 고딕" 이 설치되어 있을 경우
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 부호 깨짐 방지


scenarios = pd.DataFrame({
    "시나리오": ["기존 댐", "리파워링(보조터빈 추가)"],
    "낙차 (m)": [10, 15],
    "유량 (m³/s)": [2.5, 2.5],
    "효율 (%)": [70, 80]
})
scenarios["발전량 (kW)"] = 9.81 * 1000 * scenarios["낙차 (m)"] * scenarios["유량 (m³/s)"] * (scenarios["효율 (%)"]/100) / 1000

st.dataframe(scenarios)
