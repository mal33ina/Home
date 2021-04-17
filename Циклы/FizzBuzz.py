n = int(input("Enter the number: "))
# Условие: Нужно вывести было вместо числа кратному 3 (Solo), а кратному 5 (Learn)., и кратные одновременно 3 и 5 (SoloLearn)
# Также чтоб четные число вооще никакие не выводились, а четные выводились.
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0 and x % 2 != 0:
        print("Solo")
    elif x % 5 == 0 and x % 2 != 0:
        print("Learn")
    elif x % 2 == 0:
        continue
    else:
        print(x)







