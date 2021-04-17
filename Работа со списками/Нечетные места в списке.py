i = "Привет как твои дела вечером Мистер"
a = list(i)
b = len(a)
c = a[0:b:5]
for a in range(b):
    if a == " ":
        c.pop(" ")
    print(c)



























