# Контрольный пример (Фотография 2)
# Проверка чисел 28 и 12

for n in (28, 12):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    proper_sum = sum(i for i in divisors if i < n)
    verdict = "является совершенным" if proper_sum == n else "не является совершенным"

    print(f"--- Результаты анализа делителей ({n}) ---")
    print(f"Все делители числа {n}: {divisors}")
    print(f"Количество делителей: {len(divisors)}")
    print(f"Сумма собственных делителей: {proper_sum}")
    print(f"Вывод: число {n} {verdict}.\n")
