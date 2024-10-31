import sys


user_name = ''
password_user = ''
password_user_confirm = ''

user_select = input('Выберите действие: 1 - регистрация / 2 - вход / 0 - выход\nДействие: ')
if(user_select == '0'):
    print('Вы вышли из программы')
    sys.exit()
if user_select == '1':
    while True:
        print('Регистрация')
        user_name = input('Введите ваш логин: ')
        password_user = input('Придумайте пароль: ')
        if len(password_user) < 8:
            print('Короткий')
            continue
        elif password_user == '123':
            print('Простой')
            continue
        password_user_confirm = input('Потвердите ваш пароль: ')
        if len(password_user_confirm) < 8:
            print('Короткий')
            continue
        elif password_user != password_user_confirm:
            print('Несовпадение паролей')
            continue
        else:
            print('Успешная регистрация!')
            user_select = '2'
            break


if user_select == '2':
    while True:
        print('Вход')
        sign_user = input('Введите ваш логин: ')
        if sign_user != user_name:
            print('Нет такого логина')
            continue
        sign_password = input('Введите ваш пароль: ')
        if sign_password.isspace():
            print('Не будь петухом')

            continue
        elif sign_password == '123':
            print('Простой')
            continue
        elif len(sign_password) < 8:
            print('Короткий')
            continue
        elif sign_password != password_user:
            print('Неправильный пароль')
        else:
            print('Успешный вход')
            break

