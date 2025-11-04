import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os

# --------------------------------------------------
# 1. API Key 입력
# --------------------------------------------------
load_dotenv()
API_KEY = os.getenv("VWORLD_API_KEY")

if not API_KEY:
    raise ValueError("VWORLD API Key를 찾을 수 없습니다. .env 파일을 확인하세요.")

# --------------------------------------------------
# 2. 데이터 불러오기
# --------------------------------------------------
input_path = "data/한국수자원공사_소수력 잠재 발전 가능량 데이터_20240501.csv"
output_path_full = "댐_위도경도_자동매핑.csv"        # 전체 데이터
output_path_coords = "댐_위도경도_좌표만.csv"       # 위도·경도만 따로 저장

# 인코딩 자동 감지
try:
    df = pd.read_csv(input_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(input_path, encoding='cp949')

# --------------------------------------------------
# 3. 중복 제거
# --------------------------------------------------
df_unique = df.drop_duplicates(subset=['표준유역명']).reset_index(drop=True)

# --------------------------------------------------
# 4. 위도·경도 검색 함수
# --------------------------------------------------


def get_coords(name):
    url = (
        f"http://api.vworld.kr/req/search?"
        f"service=search&request=search&version=2.0&crs=EPSG:4326"
        f"&size=1&page=1&query={name}&type=place&key={API_KEY}"
    )
    try:
        res = requests.get(url, timeout=5).json()
        items = res.get("response", {}).get("result", {}).get("items", [])
        if not items:
            return None, None
        point = items[0]["point"]
        lat, lon = float(point["y"]), float(point["x"])
        print(f"✅ {name} → 위도:{lat}, 경도:{lon}")
        return lat, lon
    except Exception as e:
        print(f"⚠️ {name} 검색 실패: {e}")
        return None, None


# --------------------------------------------------
# 5. 위도·경도 붙이기
# --------------------------------------------------
lats, lons = [], []
for name in df_unique["표준유역명"]:
    lat, lon = get_coords(name)
    lats.append(lat)
    lons.append(lon)
    time.sleep(0.2)

df_unique["위도"] = lats
df_unique["경도"] = lons

# --------------------------------------------------
# 6. 원본 데이터와 병합
# --------------------------------------------------
df_final = pd.merge(df, df_unique[["표준유역명", "위도", "경도"]], on="표준유역명", how="left")

# --------------------------------------------------
# 7. 파일 저장
# --------------------------------------------------
# (1) 전체 데이터
df_final.to_csv(output_path_full, index=False, encoding="utf-8-sig")

# (2) 위도·경도만 따로
df_unique[["표준유역명", "위도", "경도"]].to_csv(output_path_coords, index=False, encoding="utf-8-sig")

print(f"\n💾 전체 데이터 저장 완료 → '{output_path_full}'")
print(f"📍 위도·경도만 저장 완료 → '{output_path_coords}'")
