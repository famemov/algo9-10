def f3(a):
    if not a:
        return []
    
    m = max(a)
    b = [[0] * len(a) for _ in range(m)]
    
    for i, x in enumerate(a):
        for j in range(x):
            b[j][i] = 1
    
    for i in range(m):
        c = sum(b[i])
        for j in range(len(a)):
            b[i][j] = 1 if j < c else 0
    
    r = []
    for j in range(len(a)):
        r.append(sum(b[i][j] for i in range(m)))
    
    return r

# Пример
a = [3, 1, 4, 2, 2]
print("Вход:", a)
r = f3(a)
print("Выход:", r)