import matplotlib.pyplot as plt
from modules.base_hydro import BaseHydro


class SimHydro(BaseHydro):
    def simulate(self, Q, H, eta):
        """입력값에 따른 발전량 계산"""
        rho, g = 1000, 9.81
        P = rho * g * H * Q * eta / 1000
        return round(P, 2)

    def plot_power_curve(self, Q, eta):
        """낙차 변화에 따른 발전량 그래프"""
        rho, g = 1000, 9.81
        H_values = list(range(1, 51))
        P_values = [rho * g * h * Q * eta / 1000 for h in H_values]

        plt.figure(figsize=(6, 4))
        plt.plot(H_values, P_values, color='blue')
        plt.xlabel("낙차 (m)")
        plt.ylabel("발전량 (kW)")
        plt.title("낙차 변화에 따른 발전량 곡선")
        plt.grid(True)
        return plt
