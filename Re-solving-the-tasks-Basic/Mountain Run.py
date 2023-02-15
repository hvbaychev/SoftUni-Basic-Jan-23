import math

record = float(input())
claim_metter = float(input())
time_for_metter_in_sec = float(input())

total_sec_claim = claim_metter * time_for_metter_in_sec
resistance = math.floor((claim_metter / 50)) * 30

total_time = total_sec_claim + resistance

if total_time < record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    diff = abs(total_time - record)
    print(f"No! He was {diff:.2f} seconds slower.")