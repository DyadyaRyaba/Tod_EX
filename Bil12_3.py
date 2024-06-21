import matplotlib.pyplot as plt
import numpy as np

# Создание данных
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Создание фигуры и подграфиков
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Синус
axs[0, 0].plot(x, np.sin(x), 'r-', label='sin(x)')  # красный цвет, сплошная линия
axs[0, 0].grid(True)
axs[0, 0].legend()

# Косинус
axs[0, 1].plot(x, np.cos(x), 'b--', label='cos(x)')  # синий цвет, пунктирная линия
axs[0, 1].grid(True)
axs[0, 1].legend()

# Тангенс
axs[1, 0].plot(x, np.tan(x), 'g-.', label='tan(x)')  # зеленый цвет, штрихпунктирная линия
axs[1, 0].set_ylim(-10, 10)  # ограничиваем ось y для более красивого отображения
axs[1, 0].grid(True)
axs[1, 0].legend()

# x^2 и x^3
axs[1, 1].plot(x, x**2, 'm:', label='x^2')  # пурпурный цвет, точечная линия
axs[1, 1].plot(x, x**3, 'c-', label='x^3')  # циановый цвет, сплошная линия
axs[1, 1].grid(True)
axs[1, 1].legend()

# Общий заголовок
fig.suptitle('Graphs of Various Functions', fontsize=16)

# Показать графики
plt.tight_layout(rect=[0, 0, 1, 0.96])  # для правильного размещения заголовка
plt.show()
