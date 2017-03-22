import math
def is_palindrome(n):
    s=list(str(n))
    h=math.floor(len(str(n)))
    for x in range(h):
        if s[x]!=s[h-1-x]:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))