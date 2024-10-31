def first_last(letter, st):
    f = st.find(letter)
    if f == -1:
        return None,None
    else:
        return letter[0],letter[-1]
st = input('Введите строку: ')
letter = input('Введите символ: ')
print(first_last(letter,st))
