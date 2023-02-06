start = input()
end = input()
exception = input()

combinations = 0

for x in range(ord(start), ord(end) + 1):
    if x == ord(exception):
        continue
    for y in range(ord(start), ord(end) + 1):
        if y == ord(exception):
            continue
        for z in range(ord(start), ord(end) + 1):
            if z == ord(exception):
                continue
            combinations += 1
            print(f"{chr(x)}{chr(y)}{chr(z)}", end=" ")

print(combinations)