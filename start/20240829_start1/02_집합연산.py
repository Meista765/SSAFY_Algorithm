# bit 연산자의 활용 = 집합 연산

U = 'ABCDEFGH'  # 전체 집합
A = 0b10101101  # A C D F H
B = 0b01101001  # A D F G

def print_set(U, bits):
    for i in range(len(U) - 1, -1, -1):
        if bits & (1 << i):
            print(U[i], end=' ')
    print()

print_set(U, A)
print_set(U, B)
print_set(U, A | B)
print_set(U, A & B)
print_set(U, ~A)
print_set(U, A & ~B)
print_set(U, A ^ B)
# =========================
U = set('ABCDEFGH')
A = {'A', 'C', 'D', 'F', 'H'}
B = {'A', 'D', 'F', 'G'}
print(A | B)
print(A & B)
print(U - A)
print(A - B)
print(A ^ B)
