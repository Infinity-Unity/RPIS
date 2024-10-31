def shortener(st):
    start_line = 0
    end_line = 0
    newl = ''
    y = 0
    while y < len(st):
        if st[y] == '(':
            newl += st[:y]
        if st[y] == ')':
            newl += st[y + 1:]
        y += 1
    return newl


print(shortener(input()))


