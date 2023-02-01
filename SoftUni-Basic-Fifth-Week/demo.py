a = 5
b = 10
while b != 0:
    oldB = b
    b = a % b
    a = oldB
print(a)