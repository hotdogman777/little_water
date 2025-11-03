import streamlit as st
from modules.map_hydro import MapHydro
from modules.sim_hydro import SimHydro

# 파일 경로
csv_path = "data/한국수자원공사_소수력 잠재 발전 가능량 데이터_20240501.csv"

# 객체 생성
map_obj = MapHydro(csv_path)
sim_obj = SimHydro(csv_path)

# 데이터 불러오기
map_obj.load_data()
map_obj.clean_data()

# Streamlit UI
st.title("💧 소수력 발전 시각화 및 시뮬레이터")

tab1, tab2 = st.tabs(["지도 보기", "시뮬레이션"])

with tab1:
    st.subheader("전국 소수력 잠재 발전 지도")
    folium_map = map_obj.create_map()
    st.components.v1.html(folium_map._repr_html_(), height=600)

with tab2:
    st.subheader("발전량 시뮬레이션")
    Q = st.slider("유량 (m³/s)", 0.1, 5.0, 1.0, 0.1)
    H = st.slider("낙차 (m)", 1, 50, 10)
    eta = st.slider("효율 (%)", 40, 90, 75) / 100

    P = sim_obj.simulate(Q, H, eta)
    st.metric(label="예상 발전량", value=f"{P:.2f} kW")

    plt = sim_obj.plot_power_curve(Q, eta)
    st.pyplot(plt)
