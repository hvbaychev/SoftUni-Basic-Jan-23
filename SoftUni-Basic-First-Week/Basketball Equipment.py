payPerYear = int(input())

priceShoes = payPerYear * 0.40
totalPriceShoes = payPerYear - priceShoes

priceEqiup = totalPriceShoes * 0.20
totalPriceEquip = totalPriceShoes - priceEqiup

priceBall = totalPriceEquip * 0.25

priceAcc = priceBall * 0.20

totalSum = payPerYear + totalPriceShoes + totalPriceEquip + priceBall + priceAcc

print(totalSum)
