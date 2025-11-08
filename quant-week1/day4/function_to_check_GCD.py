def gcd(a, b) -> int:
    while(b != 0):
        a, b = b, a % b
    return a

print(gcd(4, 12))
print(gcd(48, 10))
print(gcd(500, 12))
