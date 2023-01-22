length = int(input())
width = int(input())
height = int(input())
percent = int(input())

totalVolume = length * width * height
totalLitre = totalVolume * 0.001

reserveSpace = percent / 100

needLitre = totalLitre * (1 - reserveSpace)

print(needLitre)