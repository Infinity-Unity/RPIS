from collections import Counter


def top3(st):
    cleaned_string = st.replace(" ", "").lower()
    character_count = Counter(cleaned_string)
    for char, count in character_count.items():
        print(f"'{char}': {count}")

top3(input("Введите строку: "))