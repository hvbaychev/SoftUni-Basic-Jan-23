doctors = 7

period = int(input())

treat_patient = 0
untreat_patient = 0

for medp in range(1, period+1):
    new_patient = int(input())
    if medp % 3 == 0 and untreat_patient > treat_patient:
        doctors = doctors + 1

    if new_patient >= doctors:
        treat_patient += doctors
        untreat_patient += new_patient - doctors
    else:
        treat_patient += new_patient

print(f'Treated patients: {treat_patient:.0f}.')
print(f'Untreated patients: {untreat_patient:.0f}.')
