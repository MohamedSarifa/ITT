password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

if len(password) < 8:
    print("Invalid Password")
else:
    for i in range(len(password)):
        ch = password[i]
        ascii_val = ord(ch)

        if ascii_val >= 65 and ascii_val <= 90:
            upper = 1
        elif ascii_val >= 97 and ascii_val <= 122:
            lower = 1
        elif ascii_val >= 48 and ascii_val <= 57:
            digit = 1
        elif ch in ['@', '#', '$', '%', '&', '!']:
            special = 1

    if upper and lower and digit and special:
        print("Success You have entered Valid Password")
    else:
        print("You have entered Invalid Password")
