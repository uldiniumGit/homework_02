from bornyear import correct_year

while True:
    attempt_year = input('В каком году родился Пушкин?\n')
    if int(attempt_year) == correct_year:
        break
    print('неверно')

print('верно')
