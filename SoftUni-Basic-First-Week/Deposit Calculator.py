deposit = float(input())
timeDeposit = int(input())
percent = float(input())

interest = deposit * (percent / 100)
totalInterest = interest / 12
totalSum = deposit + (timeDeposit * totalInterest)

print(totalSum)