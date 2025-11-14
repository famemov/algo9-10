def run_tests():
    print("=== ТЕСТИРОВАНИЕ АЛГОРИТМОВ ===")
    
    # Импорт алгоритмов
    from sort1 import f1 as bucket_sort
    from sort2 import f2 as pancake_sort
    from sort3 import f3 as bead_sort
    from search1 import f4 as jump_search
    from search2 import f5 as exponential_search
    from search3 import f6 as ternary_search
    
    test_count = 0
    passed_count = 0
    
    # Тест 1: блочная сортировка
    print("\n1. Тест блочной сортировки")
    input_data = [0.8, 0.2, 0.6, 0.4, 0.1]
    expected = [0.1, 0.2, 0.4, 0.6, 0.8]
    result = bucket_sort(input_data)
    test_count += 1
    if result == expected:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
        print(f"  Ожидалось: {expected}")
        print(f"  Получено: {result}")
    
    # Тест 2: блинная сортировка
    print("\n2. Тест блинной сортировки")
    input_data = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    result = pancake_sort(input_data.copy())
    test_count += 1
    if result == expected:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
        print(f"  Ожидалось: {expected}")
        print(f"  Получено: {result}")
    
    # Тест 3: сортировка бусинами
    print("\n3. Тест сортировки бусинами")
    input_data = [2, 4, 1, 3, 2]
    expected = [1, 2, 2, 3, 4]
    result = bead_sort(input_data)
    test_count += 1
    if result == expected:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
        print(f"  Ожидалось: {expected}")
        print(f"  Получено: {result}")
    
    # Тест 4-6: алгоритмы поиска
    test_array = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("\n4. Тест поиска скачками")
    test_count += 1
    if jump_search(test_array, 7) == 3:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
    
    print("\n5. Тест экспоненциального поиска")
    test_count += 1
    if exponential_search(test_array, 9) == 4:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
    
    print("\n6. Тест тернарного поиска")
    test_count += 1
    if ternary_search(test_array, 5) == 2:
        print("✓ Пройден")
        passed_count += 1
    else:
        print("✗ Не пройден")
    
    # Итоги
    print(f"\n=== РЕЗУЛЬТАТЫ ===")
    print(f"Пройдено: {passed_count}/{test_count}")
    print(f"Успешность: {passed_count/test_count*100:.1f}%")

if __name__ == "__main__":
    run_tests()