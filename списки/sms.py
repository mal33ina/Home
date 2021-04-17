sms = input("Напишите sms: ")
b = len(sms)
if b % 60 == 0:
    print(b, "sms")
else:
    print(b//60+1, "sms")











