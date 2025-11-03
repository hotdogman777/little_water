import pandas as pd

# CSV 파일 경로
file_path = "data/한국수자원공사_소수력 잠재 발전 가능량 데이터_20240501.csv"

# 파일 읽기 (인코딩 자동 시도)
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

# 중복 제거된 댐 이름만 추출
unique_dams = df['표준유역명'].dropna().unique()
unique_dams = sorted(unique_dams)

# DataFrame으로 변환
df_unique = pd.DataFrame(unique_dams, columns=['표준유역명'])

# 새 파일로 저장 (.csv 또는 .txt 가능)
save_path = "고유_댐이름_목록.csv"
df_unique.to_csv(save_path, index=False, encoding='utf-8-sig')

print(f"✅ 중복 없는 댐 이름이 '{save_path}' 파일로 저장되었습니다.")
