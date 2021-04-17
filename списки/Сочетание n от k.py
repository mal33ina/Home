def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact


def loter(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))


k = int(input("Введи количество чисел которые надо угодать: "))
n = int(input("Введите из какого количество чисел нужно угодать: "))
print(loter(n, k))





