start = int(input())
end = int(input())
magic = int(input())
counter = 0

for num1 in range(start, end+1):
    for num2 in range(start, end+1):
        counter += 1
        if num1+num2 == magic:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic})")
            exit()

print(f"{counter} combinations - neither equals {magic}")
