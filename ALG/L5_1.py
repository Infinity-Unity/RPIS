total = 100
while total > 0:
    n = int(input())
    if n > total:
        print('Недопустимая операция!')
        break
    total -= n
print("Ресурс исчерпан")
