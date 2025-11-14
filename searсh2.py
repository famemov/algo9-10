def f5(a, x):
    def bs(arr, l, r, t):
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == t:
                return m
            elif arr[m] < t:
                l = m+1
            else:
                r = m-1
        return -1
    
    n = len(a)
    if n == 0:
        return -1
    
    if a[0] == x:
        return 0
    
    i = 1
    while i < n and a[i] <= x:
        i *= 2
    
    return bs(a, i//2, min(i, n-1), x)

# Пример
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x = 10
print("Массив:", a)
print("Поиск:", x)
r = f5(a, x)
print("Найден на:", r)