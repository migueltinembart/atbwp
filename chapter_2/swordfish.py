while True:
    print("Who are you")
    name = input()
    if name != "Joe":
        continue
    count = 0
    while count != 3:
        print("Hello Joe. What is the password?")
        password = input()
        if password == "swordfish":
            break
        else:
            count = count + 1
            print('tries left: {} , {}'.format(3 - count))
            continue
print("access granted")
