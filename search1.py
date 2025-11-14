# ПОИСК СКАЧКАМИ (JUMP SEARCH)
import math

def f4(a, x):
    """
    Алгоритм поиска скачками в отсортированном массиве
    Сначала прыгает, затем линейно ищет в блоке
    """
    n = len(a)
    if n == 0:
        return -1
    
    # Определяем размер прыжка
    s = int(math.sqrt(n))
    p = 0
    
    # Фаза прыжков
    while p < n and a[min(p+s, n)-1] < x:
        p += s
    
    # Линейный поиск в блоке
    for i in range(p, min(p+s, n)):
        if a[i] == x:
            return i
        if a[i] > x:
            break
    
    return -1

# Пример использования
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 7
    print("Поиск скачками:")
    print("Массив:", a)
    print("Ищем:", x)
    print("Позиция:", f4(a, x))