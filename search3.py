def f6(a, x):
    def ts(l, r, t):
        if l > r:
            return -1
        
        m1 = l + (r-l)//3
        m2 = r - (r-l)//3
        
        if a[m1] == t:
            return m1
        if a[m2] == t:
            return m2
        
        if t < a[m1]:
            return ts(l, m1-1, t)
        elif t > a[m2]:
            return ts(m2+1, r, t)
        else:
            return ts(m1+1, m2-1, t)
    
    return ts(0, len(a)-1, x)

# Пример
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x = 7
print("Массив:", a)
print("Поиск:", x)
r = f6(a, x)
print("Найден на:", r)