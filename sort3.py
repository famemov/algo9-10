# СОРТИРОВКА БУСИНАМИ (BEAD SORT)
def f3(a):
    """
    Гравитационная сортировка для неотрицательных целых чисел
    Моделирует падение бусин под действием гравитации
    """
    if not a:
        return []
    
    m = max(a)
    # Создаем матрицу бусин
    b = [[0] * len(a) for _ in range(m)]
    
    # Расставляем бусины
    for i, x in enumerate(a):
        for j in range(x):
            b[j][i] = 1
    
    # Симулируем гравитацию
    for i in range(m):
        c = sum(b[i])
        for j in range(len(a)):
            b[i][j] = 1 if j < c else 0
    
    # Считываем результат
    r = []
    for j in range(len(a)):
        r.append(sum(b[i][j] for i in range(m)))
    
    return r

# Пример использования
if __name__ == "__main__":
    a = [3, 1, 4, 2, 2]
    print("Сортировка бусинами:")
    print("Вход:", a)
    print("Выход:", f3(a))