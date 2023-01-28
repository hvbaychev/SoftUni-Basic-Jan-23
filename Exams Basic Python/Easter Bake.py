import math

bread = int(input())

total_need_sugar = 0
total_need_flour = 0
sugar_pack_gram = 950
flour_pack_gram = 750
max_used_sugar = 0
max_used_flour = 0
pack_sugar = 0
pack_flour = 0

for _ in range(bread):
    sugar_used = int(input())
    flour_used = int(input())

    total_need_sugar += sugar_used
    pack_sugar = total_need_sugar / sugar_pack_gram

    total_need_flour += flour_used
    pack_flour = total_need_flour / flour_pack_gram

    max_used_sugar = max(max_used_sugar, sugar_used)
    max_used_flour = max(max_used_flour, flour_used)

print(f"Sugar: {math.ceil(pack_sugar)}")
print(f"Flour: {math.ceil(pack_flour)}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")