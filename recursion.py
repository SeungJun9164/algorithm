# 팩토리얼
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

# 최대공약수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(60, 24))

# 피보나치
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n):
        return fibo(n-1) + fibo(n-2)
print(fibo(8))

# 하노이탑
_sum = 1
def hanoi(n, from_pos, to_pos, temp_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return 1
    hanoi(n-1, from_pos, temp_pos, to_pos)
    print(from_pos, "->", to_pos)
    hanoi(n-1, temp_pos, to_pos, from_pos)

for i in range(2):
    _sum = _sum * 2 + 1
print(_sum, hanoi(3,1,3,2))