def search_substr(subst, st):
    if st.find(subst) == -1:
        return 'Мимо!'
    else:
        return 'Есть контакт!'
st = input('Введите строку: ')
subst = input('Введите подстроку: ')
print(search_substr(subst,st))

