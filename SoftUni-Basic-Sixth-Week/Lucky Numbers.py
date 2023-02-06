n = int(input())

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            for l in range(1, n):
                if i+j == k+l and (i+j) % n == 0:
                    print(f"{i}{j}{k}{l}", end=' ')
