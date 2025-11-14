print("=== ДЕМОНСТРАЦИЯ АЛГОРИТМОВ ===")

# Импорт всех алгоритмов
from sort1 import f1 as bucket_sort
from sort2 import f2 as pancake_sort
from sort3 import f3 as bead_sort
from search1 import f4 as jump_search
from search2 import f5 as exponential_search
from search3 import f6 as ternary_search

print("\n--- АЛГОРИТМЫ СОРТИРОВКИ ---")

# Тест блочной сортировки
a1 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print(f"Блочная сортировка:")
print(f"Вход: {a1}")
print(f"Выход: {bucket_sort(a1)}")

# Тест блинной сортировки
a2 = [3, 1, 4, 2, 6, 5]
print(f"\nБлинная сортировка:")
print(f"Вход: {a2}")
print(f"Выход: {pancake_sort(a2.copy())}")

# Тест сортировки бусинами
a3 = [3, 1, 4, 2, 2]
print(f"\nСортировка бусинами:")
print(f"Вход: {a3}")
print(f"Выход: {bead_sort(a3)}")

print("\n--- АЛГОРИТМЫ ПОИСКА ---")

# Тест поиска в отсортированном массиве
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 7

print(f"Массив: {arr}")
print(f"Ищем: {target}")

print(f"\nПоиск скачками: позиция {jump_search(arr, target)}")
print(f"Экспоненциальный поиск: позиция {exponential_search(arr, target)}")
print(f"Тернарный поиск: позиция {ternary_search(arr, target)}")

# Поиск несуществующего элемента
print(f"\nПоиск несуществующего элемента (20):")
print(f"Поиск скачками: {jump_search(arr, 20)}")
print(f"Экспоненциальный: {exponential_search(arr, 20)}")
print(f"Тернарный: {ternary_search(arr, 20)}")