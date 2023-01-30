rent_hall = int(input())

statuette = rent_hall * 0.70
catering = statuette * 0.85
music = catering / 2

total_sum = statuette + catering + music + rent_hall

print(f'{total_sum:.2f}')