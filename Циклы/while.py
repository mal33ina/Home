for x in 1, 2, 3, 4, 5:
    print(x**2)

c = 1
while c <= 10:
    print(c**2)
    c += 1


Line = input()
while Line != "end":
    i = int(Line)
    print(i**2)


x = int(input("ВВеди число: "))
while x > 0:
    c = x % 10
    print(c**2)
    x //= 10


