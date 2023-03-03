def reverseString(string):
    a=""
    for i in string:
        a=i+a
    return a
a1 = input()
print(reverseString(a1))

