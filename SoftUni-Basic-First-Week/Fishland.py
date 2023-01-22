priceSkumria = float(input())
priceCaca = float(input())

kgPalamud = float(input())
kgSafrid = float(input())
kgMidi = float(input())

pricePalamud = priceSkumria * 1.60
priceSafrid = priceCaca * 1.80
priceMidi = 7.50


totalSumPalamud = pricePalamud * kgPalamud
totalSumSafrid = priceSafrid * kgSafrid
totalSumMidi = kgMidi * priceMidi
totalSumForPay = totalSumPalamud + totalSumSafrid + totalSumMidi

print('%.2f' %totalSumForPay)

