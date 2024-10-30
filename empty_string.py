
while True:
    stroka = input('>>> ')
    if(stroka.isspace() or stroka == ''):
        print('Пустая строка')
        break
    print(stroka)