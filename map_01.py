import folium
import pandas as pd

# 데이터 불러오기
df = pd.read_csv("댐_위도경도_자동매핑.csv", encoding="utf-8")

# 지도 초기화 (대한민국 중심)
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 댐별 마커 추가
for _, row in df.iterrows():
    if pd.notnull(row["위도"]) and pd.notnull(row["경도"]):
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=5 + (row["발전량"] / df["발전량"].max()) * 10,  # 발전량 비례 크기
            color="blue",
            fill=True,
            fill_opacity=0.6,
            popup=f"""
                <b>{row['표준유역명']}</b><br>
                유량: {row['유량']} m³/s<br>
                발전량: {row['발전량']} kW<br>
                위도: {row['위도']}, 경도: {row['경도']}
            """,
        ).add_to(m)

# 저장
m.save("소수력_지도.html")
print("✅ 지도 저장 완료 → '소수력_지도.html' 파일 열어보세요.")
