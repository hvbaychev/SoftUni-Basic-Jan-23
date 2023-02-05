n = int(input())
count = 0

for x1 in range(0,n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            product = x1 + x2 + x3
            if product == n:
                count += 1
print(count)