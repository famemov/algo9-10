def f1(a):
    if not a:
        return a
    
    n = len(a)
    b = [[] for _ in range(n)]
    
    for x in a:
        i = int(x * n)
        b[i].append(x)
    
    for c in b:
        c.sort()
    
    d = []
    for c in b:
        d.extend(c)
    
    return d

# Пример
a = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Вход:", a)
r = f1(a)
print("Выход:", r)