import cvxpy as cp

# Переменные (количество яблок и бананов)
d_apple = cp.Variable(integer=True)  # Целое число (не дробные яблоки)
d_banana = cp.Variable(integer=True)

# Целевая функция: минимизируем стоимость
cost = 45 * d_apple + 54 * d_banana
objective = cp.Minimize(cost)

# Ограничение: витамины >= 10
vitamins = 110 * d_apple + 130 * d_banana >= 2800

# Решаем задачу
prob = cp.Problem(objective, [vitamins, d_apple >= 0, d_banana >= 0])
prob.solve()

# Выводим результат
print(f"Купить {d_apple.value} яблок и {d_banana.value} бананов")
print(f"Стоимость: {prob.value} рублей")