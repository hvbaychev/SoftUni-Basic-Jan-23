heightHouse = float(input())
lengthHouse = float(input())
heightRoofTrSide = float(input())

greenColPerLiter = 3.4
redColPerLiter = 4.3

doorSpace = 1.2 * 2
windowsSpace = (1.5 * 1.5) * 2

sidesWall = (heightHouse * lengthHouse) * 2 - windowsSpace
backSideWall = (heightHouse * heightHouse) * 2 - doorSpace

totalAreaWalls = sidesWall + backSideWall

totalGreenCol = totalAreaWalls / greenColPerLiter
print('%.2f' % totalGreenCol)

rectangleRoof = 2
triangleRoof = 2

rectangleAreaOfRoof = rectangleRoof * (heightHouse * lengthHouse)
triangleAreaOfRoof = triangleRoof * (heightHouse * heightRoofTrSide / 2)

totalAreaOfRoof = rectangleAreaOfRoof + triangleAreaOfRoof

totalRedCol = totalAreaOfRoof / redColPerLiter
print('%.2f' % totalRedCol)
