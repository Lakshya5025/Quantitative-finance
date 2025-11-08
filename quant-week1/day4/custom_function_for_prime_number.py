def isPrime(num)->bool:
    for i in range (2, num//2 + 1):
        if(num % i == 0): return False
    return True

print(isPrime(5))
print(isPrime(4))
print(isPrime(2))
print(isPrime(1))
print(isPrime(20))