def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    ratios = {item: info['calories'] / info['cost'] for item, info in items.items()}
    # Сортування страв за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, ratio in sorted_items:
        cost = items[item]['cost']
        calories = items[item]['calories']
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Перетворення даних у формат для динамічного програмування
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    
    n = len(item_names)
    # Створення таблиці для зберігання максимальних калорій для кожного підбюджету
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнення таблиці динамічного програмування
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення списку вибраних страв
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]
    
    return selected_items, dp[n][budget]

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Greedy Algorithm Result:")
greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Selected Items:", greedy_items)
print("Total Calories:", greedy_calories)

print("\nDynamic Programming Result:")
dp_items, dp_calories = dynamic_programming(items, budget)
print("Selected Items:", dp_items)
print("Total Calories:", dp_calories)
