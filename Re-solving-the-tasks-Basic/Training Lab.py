length = float(input())
width = float(input())
coloumns = (width * 100 - 100) // 70
rows = length * 100 // 120
result = coloumns * rows - 3
print(result)