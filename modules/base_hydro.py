import pandas as pd


class BaseHydro:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        """CSV 불러오기"""
        self.df = pd.read_csv(self.csv_path, encoding='utf-8')
        print("✅ 데이터 불러오기 완료:", self.df.shape)
        return self.df

    def clean_data(self):
        """결측치 처리 및 기본 전처리"""
        self.df = self.df.dropna(subset=['위도', '경도'])
        self.df = self.df[self.df['예상발전량(kW)'] > 0]
        print("🧹 데이터 정제 완료")
        return self.df
