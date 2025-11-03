import folium
from modules.base_hydro import BaseHydro


class MapHydro(BaseHydro):
    def create_map(self):
        """Folium 지도 생성"""
        m = folium.Map(location=[36.5, 127.5], zoom_start=7)

        for _, row in self.df.iterrows():
            folium.CircleMarker(
                location=[row['위도'], row['경도']],
                radius=row['예상발전량(kW)'] * 0.05,
                color='blue',
                fill=True,
                fill_opacity=0.6,
                popup=f"{row['지점명']}<br>예상발전량: {row['예상발전량(kW)']:.2f} kW"
            ).add_to(m)

        return m
