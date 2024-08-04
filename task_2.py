import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, x, y, angle, length, level):
    if level == 0:
        return

    # Визначення кінцевих координат гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малювання гілки
    ax.plot([x, x_end], [y, y_end], 'k-', lw=2)

    # Рекурсивний виклик для лівої і правої гілок
    new_length = length * 0.7  # Модифікація довжини для наступних гілок
    draw_tree(ax, x_end, y_end, angle + np.pi / 6, new_length, level - 1)
    draw_tree(ax, x_end, y_end, angle - np.pi / 6, new_length, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
    
    if level < 0:
        print("Рівень рекурсії має бути невід'ємним числом.")
        return

    # Налаштування графіка
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    # Початкові координати і параметри
    x_start, y_start = 0, 0
    initial_length = 100
    initial_angle = np.pi / 2  # Вертикально вверх

    # Розпочати малювання дерева
    draw_tree(ax, x_start, y_start, initial_angle, initial_length, level)

    plt.show()

if __name__ == "__main__":
    main()
