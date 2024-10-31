def camel(st):
    news = ''
    for i in range(len(st) ):
        if i % 2 == 0:
            news += st[i].upper()
        else:
            news += st[i].lower()
    return news
print(camel(input('Введите строку: ')))
