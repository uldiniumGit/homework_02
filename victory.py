'''
Викторина с датами рождения известных музыкантов.
'''


# Функция для проверки ответа
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    else:
        return 0


# Правильные ответы для каждой знаменитости
Mozart_birthday_year = 1756
Bach_birthday_year = 1685
Vivaldi_birthday_year = 1678
Grieg_birthday_year = 1843
Liszt_birthday_year = 1811

# Цикл с викториной
while True:
    # Переменная для подсчета количества правильных ответов
    correct_answers = 0

    # Задаем участнику викторины вопросы, записываем его ответы в переменные и переводим их в тип int
    Mozart_attempt = int(input('введите год рождения Моцарта\n'))
    Bach_attempt = int(input('введите год рождения Баха\n'))
    Vivaldi_attempt = int(input('введите год рождения Вивальди\n'))
    Grieg_attempt = int(input('введите год рождения Грига\n'))
    Liszt_attempt = int(input('введите год рождения Листа\n'))

    # Проверяем ответы
    correct_answers += check_answer(Mozart_attempt, Mozart_birthday_year)
    correct_answers += check_answer(Bach_attempt, Bach_birthday_year)
    correct_answers += check_answer(Vivaldi_attempt, Vivaldi_birthday_year)
    correct_answers += check_answer(Grieg_attempt, Grieg_birthday_year)
    correct_answers += check_answer(Liszt_attempt, Liszt_birthday_year)

    # Переменная для неправильных ответов
    incorrect_answers = 5 - correct_answers

    # Выводим в терминал количество правильных ответов
    print('Количество правильных ответов', correct_answers)

    # Выводим в терминал количество неправильных ответов
    print('Количество неправильных ответов', incorrect_answers)

    # Выводим в терминал процент правильных ответов
    print('Процент правильных ответов', correct_answers * 100 / 5)

    # Выводим в терминал процент неправильных ответов
    print('Процент неправильных ответов', incorrect_answers * 100 / 5)

    play_again = input('\nХотите сыграть еще раз?\n')
    if play_again == 'да':
        pass
    else:
        break
