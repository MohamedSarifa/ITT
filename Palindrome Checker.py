from collections import deque
def is_palindrome(s):
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return "Not a Palindrome"
    return "Palindrome"
print(is_palindrome("level"))
