
while True:
    user_input = int(input('>>> '))
    if(user_input > 1000):
        print(user_input - (user_input * 0.05))
    elif(user_input < 0):
        break

    print(user_input)