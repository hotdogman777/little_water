import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"  # "맑은 고딕" 이 설치되어 있을 경우
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 부호 깨짐 방지


rain = np.linspace(0, 300, 50)  # mm 단위 강수량
Q = rain * 0.01  # 단순 가정: 강수량 1mm 증가 → 유량 0.01 증가
H = 10
eta = 0.75

P = 1000 * 9.81 * H * Q * eta / 1000

plt.plot(rain, P)
plt.xlabel("강수량 (mm)")
plt.ylabel("발전량 (kW)")
plt.title("강수량 변화에 따른 발전량 시뮬레이션")
st.pyplot(plt)
