import math

def f4(a, x):
    n = len(a)
    if n == 0:
        return -1
    
    s = int(math.sqrt(n))
    p = 0
    
    while p < n and a[min(p+s, n)-1] < x:
        p += s
    
    for i in range(p, min(p+s, n)):
        if a[i] == x:
            return i
        if a[i] > x:
            break
    
    return -1

# Пример
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
print("Массив:", a)
print("Поиск:", x)
r = f4(a, x)
print("Найден на:", r)