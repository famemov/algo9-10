def f2(a):
    def flip(arr, k):
        i = 0
        while i < k // 2:
            arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
            i += 1
    
    n = len(a)
    for s in range(n, 1, -1):
        m = a.index(max(a[:s]))
        
        if m != s-1:
            if m != 0:
                flip(a, m+1)
            flip(a, s)
    
    return a

# Пример
a = [3, 1, 4, 2, 6, 5]
print("Вход:", a)
r = f2(a.copy())
print("Выход:", r)