from math import floor

numberPages = int(input())
readPagesForHour = int(input())
daysToEnd = int(input())

totalTimeForRead = numberPages / readPagesForHour
needHourPerDay = totalTimeForRead / daysToEnd

print(floor(needHourPerDay))