length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_litter = volume / 1000
unspace = percent / 100
water = volume_litter * (1-unspace)
print(water)