n = float(input())
first_year = n+(n*0.05)
second_year = first_year + (first_year*0.05)
third_year = second_year + (second_year*0.05)
print(f'{first_year:.2f}')
print(f'{second_year:.2f}')
print(f'{third_year:.2f}')