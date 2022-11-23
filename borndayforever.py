from bornyear import correct_year, correct_day

while True:
    attempt_year = input('В каком году родился Пушкин?\n')
    if int(attempt_year) == correct_year:
        while True:
            attempt_day = input('день и месяц рождения Пушкина в формате 01.01\n')
            if attempt_day == correct_day:
                break
            print('неверно')
        break
    print('неверно')

print('верно')
