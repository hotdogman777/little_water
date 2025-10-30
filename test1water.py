import streamlit as st
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"  # "맑은 고딕" 이 설치되어 있을 경우
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 부호 깨짐 방지

st.title("💧 소수력 발전 시뮬레이터")

# 입력값 슬라이더
Q = st.slider("유량 (m³/s)", 0.1, 5.0, 1.0, 0.1)
H = st.slider("낙차 (m)", 1, 50, 10)
eta = st.slider("효율 (%)", 40, 90, 75) / 100

# 발전량 계산
rho, g = 1000, 9.81
P = rho * g * H * Q * eta / 1000  # kW 단위

st.metric(label="예상 발전량", value=f"{P:.2f} kW")

# 그래프: 낙차 변화에 따른 발전량
H_values = list(range(1, 51))
P_values = [rho * g * h * Q * eta / 1000 for h in H_values]

plt.plot(H_values, P_values)
plt.xlabel("낙차 (m)")
plt.ylabel("발전량 (kW)")
st.pyplot(plt)
