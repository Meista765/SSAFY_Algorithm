#### function call ####

def f2(d, c):
    return d - c

def f1(b, a):
    c = a + b
    d = 10
    return f2(c, d)

a = 10
b = 20
print(f1(a, b)) # 20