import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры планера и движения
mass = 2.5  # масса планера (кг)
g = 9.81  # ускорение свободного падения (м/с²)
initial_height = 1000.0  # начальная высота сброса (м)
initial_velocity = 0.0  # начальная скорость (м/с)
air_resistance_coefficient = 0.3
cross_sectional_area = 0.2  # площадь поперечного сечения (м²)
air_density = 1.225  # плотность воздуха (кг/м³)

# Расчет времени планирования
target_velocity = 170.0  # целевая скорость планирования (м/с)
time_to_target_velocity = (target_velocity - initial_velocity) / g

# Создание функции для анимации
def animate(frame):
    time = frame / 10.0  # шаг времени для анимации
    if time < time_to_target_velocity:
        # Планер свободно падает
        current_height = initial_height - 0.5 * g * time ** 2
        current_velocity = initial_velocity + g * time
    else:
        # Планер планирует
        current_height = initial_height - 0.5 * g * time_to_target_velocity ** 2 + target_velocity * (time - time_to_target_velocity)
        current_velocity = target_velocity

    plt.clf()
    plt.plot(0, current_height, 'ro', markersize=10)  # положение планера
    plt.xlim(-10, 10)
    plt.ylim(0, initial_height + 100)
    plt.xlabel('Горизонтальное расстояние (м)')
    plt.ylabel('Высота (м)')
    plt.title('Движение планера')
    plt.grid(True)

# Создание анимации
fig = plt.figure()
ani = FuncAnimation(fig, animate, frames=range(0, int(time_to_target_velocity * 10) + 10), repeat=False, interval=100)
plt.show()
