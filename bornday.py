from bornyear import correct_year, correct_day

attempt_year = input('В каком году родился Пушкин?\n')

if int(attempt_year) == correct_year:
    attempt_day = input('день и месяц рождения Пушкина в формате 01.01\n')
    if attempt_day == correct_day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
