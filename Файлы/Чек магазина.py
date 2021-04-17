import os, codecs

n = u'' + 'D:/Chek.txt'
prod_dict = {'хлеб': '2 рубля', 'макароны': '3 рубля', 'iogurt': '1 рубль', 'oil': '4 рубля'}
seller = input('Кто продавец?\n ')
f1 = codecs.open(n, 'a', 'utf-8')
f1.write(u'' + 'ОАО MARKET\n ')
f1.write(u'' + f'Продавец: {seller}\n')
f1.write(u'' + ' Покупки:\n')
for prod in prod_dict.items():
    f1.write(str(prod)+'\n')
f1.write(u'' + '\nСпасибо!')
f1.close()

if(os.path.exists(n)):
    f1 = codecs.open(n, 'r', 'utf-8')
    text = f1.read()
    f1.close()
    print(text)
