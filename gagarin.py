spisok = []

for i in range(1,6):
    height = int(input('>>> '))
    if height > 150 and height < 190:
        spisok.append(height)
    else:
        continue
print(spisok)
print('!')