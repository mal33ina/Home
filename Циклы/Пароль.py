password = input("введите восьми значное число без пробелов, используя большие и маленькие буквы, и как минимум одну цифру ")
s = password
probel = False
b_b = False
m_b = False
chislo = False
for bukva in s:
	if bukva.isupper():
		b_b = True
	if bukva.isspace():
		probel = True
	if bukva.islower():
		m_b = True
	if bukva.isdigit():
		chislo = True
if b_b and m_b and (not probel) and chislo: 
	print(f"пароль {password} сохранен")
else:
	if not b_b:
		print("нет прописных букв")
	if not m_b:
		print("нет строчных букв")
	if not chislo:
		print("нет числа")
	if probel:
		print("пароль не подходит т.к. есть пробел")
