import requests
from dotenv import load_dotenv
import os

# .env 불러오기 (.env 안에는 VWORLD_API_KEY=xxxx 형태로 저장되어 있어야 함)
load_dotenv()
API_KEY = os.getenv("VWORLD_API_KEY")

if not API_KEY:
    raise ValueError("VWORLD API Key를 찾을 수 없습니다. .env 파일을 확인하세요.")


def get_coords(name):
    """입력한 이름으로 VWORLD API를 통해 좌표(위도, 경도) 검색"""
    url = (
        f"http://api.vworld.kr/req/search?"
        f"service=search&request=search&version=2.0&crs=EPSG:4326"
        f"&size=1&page=1&query={name}&type=place&key={API_KEY}"
    )
    try:
        res = requests.get(url, timeout=5).json()
        items = res.get("response", {}).get("result", {}).get("items", [])
        if not items:
            print(f"❌ '{name}' 의 위치를 찾을 수 없습니다.")
            return None, None
        point = items[0]["point"]
        lat, lon = float(point["y"]), float(point["x"])
        print(f"✅ {name} → 위도: {lat}, 경도: {lon}")
        return lat, lon
    except Exception as e:
        print(f"⚠️ 검색 중 오류 발생: {e}")
        return None, None


# ------------------------------
# 예시 실행
# ------------------------------
if __name__ == "__main__":
    while True:
        name = input("\n검색할 댐 이름을 입력하세요 (종료하려면 q): ")
        if name.lower() == "q":
            break
        get_coords(name)
