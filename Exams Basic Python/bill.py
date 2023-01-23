char1 = "**"
char2 = "================================"
str1 = """      Coding Temple, Inc \n      283 Franklin Str. \n      Boston, MA"""

str2 = "Product Name"
name1 = "Books"
name2 = "Computer"
name3 = "Monitor"

str3 = "Product Price"
price1 = 49.95
price2 = 579.99
price3 = 124.89
total = 0
str4 = "Total"

str5 = "Thanks for shoppng with us today!"

total = price1+price2+price3

print(char1)
print(str1)
print(char2)
print("{}   {}".format(str2,str3))
print("{}          ${}".format(name1,price1))
print("{}       ${}".format(name2,price2))
print("{}        ${}".format(name3,price3))
print(char2)
print("               {}".format(str4))
print("               $",total)
print(char2)
print(str5)
print(char1)