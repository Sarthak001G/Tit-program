T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    price_C = (B / A) * C
    print(int(price_C))