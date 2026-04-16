email = input("Enter email: ")

at_count = 0
dot_after_at = 0
at_pos = -1
space_found = 0

for i in range(len(email)):
    ch = email[i]

    if ch == ' ':
        space_found = 1

    if ch == '@':
        at_count += 1
        at_pos = i

    if at_pos != -1 and ch == '.':
        dot_after_at = 1

if (
    at_count == 1 and
    at_pos != 0 and
    at_pos != len(email) - 1 and
    dot_after_at == 1 and
    email[len(email) - 1] != '.' and
    space_found == 0
):
    print("Success You have entered Valid Email")
else:
    print("You have entered Invalid Email")
