roll_paper = int(input())
roll_linen = int(input())
glue = float(input())
discount = int(input())

PACKING_PAPER = 5.80 * roll_paper
LINEN = 7.20 * roll_linen
GLUE_PRICE = 1.20 * glue

total = (PACKING_PAPER + LINEN + GLUE_PRICE)
total_discoutn = total * (discount/100)
final_price = total - total_discoutn

print(f'{final_price:.3f}')





