def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
prime_count = 0

for i in range(1, n+1):
    if is_prime(i):
        prime_count += 1
        for j in range(1, i+1):
            if is_prime(j):
                print(1, end='')
            else:
                print(0, end='')
        print()

print()
