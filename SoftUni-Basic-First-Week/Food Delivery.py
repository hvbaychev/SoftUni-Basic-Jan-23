chicкenMenu = 10.35
fishMenu = 12.40
vegMenu = 8.15
delivery = 2.50

numberChickenMenu = int(input())
numberFishMenu = int(input())
numberVegMenu = int(input())

priceChickenMenu = chicкenMenu * numberChickenMenu
priceFishMenu = fishMenu * numberFishMenu
priceVegMenu = vegMenu * numberVegMenu

totalPriceMenu = priceChickenMenu + priceFishMenu + priceVegMenu

desertPrice = totalPriceMenu * 0.20

finalPriceAll = totalPriceMenu + desertPrice + delivery

print(finalPriceAll)