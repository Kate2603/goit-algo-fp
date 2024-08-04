import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    # Підрахунок кількості появ кожної можливої суми
    sum_counts = [0] * 13  # Індекси 0-12, 0 і 1 не використовуються

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = [count / num_rolls for count in sum_counts[2:]]
    
    return probabilities

def plot_probabilities(probabilities):
    possible_sums = list(range(2, 13))
    plt.figure(figsize=(10, 6))
    plt.bar(possible_sums, probabilities, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.grid(axis='y')
    plt.xticks(possible_sums)
    plt.show()

# Основна частина програми
num_rolls = 100000  # Кількість кидків
probabilities = monte_carlo_simulation(num_rolls)
plot_probabilities(probabilities)

# Порівняння з аналітичними розрахунками
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

print("\nАналіз результатів:")
for sum_, prob in analytical_probabilities.items():
    print(f"Сума {sum_}: Аналізована ймовірність = {prob:.4f}, Симуляційна ймовірність = {probabilities[sum_ - 2]:.4f}")
