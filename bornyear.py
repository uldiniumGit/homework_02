correct_year = 1799
correct_day = '10.06'

if __name__ == "__main__":
    attempt_year = input('В каком году родился Пушкин?\n')

    if int(attempt_year) == correct_year:
        print('верно\n')
    else:
        print('неверно\n')
