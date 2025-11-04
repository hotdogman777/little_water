import pandas as pd
import folium

# 1️⃣ CSV 불러오기
df = pd.read_csv("주요_댐_좌표.csv", encoding="utf-8")

# 2️⃣ 지도 초기화 (대한민국 중심)
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 3️⃣ 아이콘 파일 경로 (너가 업로드한 파일)
icon_path = "dam_icon.png"

# 4️⃣ 댐별 마커 추가 (MarkerCluster 없음)
for _, row in df.iterrows():
    name = row["댐이름"]
    lat = float(row["위도"])
    lon = float(row["경도"])

    # 커스텀 아이콘 설정
    dam_icon = folium.CustomIcon(
        icon_image=icon_path,
        icon_size=(40, 40)  # 크기 조절 가능 (30,30도 깔끔)
    )

    # 팝업 내용
    popup_html = f"""
    <b>{name}</b><br>
    위도: {lat:.6f}<br>
    경도: {lon:.6f}
    """

    # 마커 추가 (클러스터 사용 안 함)
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_html, max_width=300),
        icon=dam_icon
    ).add_to(m)

# 5️⃣ 지도 저장
m.save("댐_아이콘지도_고정.html")
print("✅ '댐_아이콘지도_고정.html' 파일이 생성되었습니다!")
