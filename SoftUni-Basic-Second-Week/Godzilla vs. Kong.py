budjetMovies = float(input())
numberStatist = int(input())
priceSuitStat = float(input())


decorPrice = budjetMovies * 0.10
allClothesPrice = numberStatist * priceSuitStat

if numberStatist > 150:
    allClothesPrice = allClothesPrice * 0.90

totalExpenses = allClothesPrice + decorPrice

diff = abs(totalExpenses - budjetMovies)

if budjetMovies >= totalExpenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")