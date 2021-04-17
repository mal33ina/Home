import datetime

def time():
    today = datetime.datetime.today()
    return today.strftime("%Y")


class Resume:
    def __init__(self, objname, objsurname, objage, obgeducation, objfav_rog_lang):
        self.name = objname
        self.surname = objsurname
        self.age = objage
        self.education = obgeducation
        self.fav_rog_lang = objfav_rog_lang
        self.year = int(time()) - int(self.age)


class New_resume(Resume):
    def __init__(self,objname, objsurname, objage, obgeducation, objfav_rog_lang, obgjob, obgwork):
        Resume.__init__(self, objname, objsurname, objage, obgeducation, objfav_rog_lang)
        self.job = obgjob
        self.work = obgwork




My_Resume = Resume('Александр', 'Малиновский', '33', 'Высшее', 'Питон')
My_Resume1 = New_resume('Александр', 'Малиновский', '33', 'Высшее', 'Питон', 'ЦДИ', 'Инженер')


print(My_Resume1.job, My_Resume1.work)
print('Name:', My_Resume.name)
print('Surname:', My_Resume.surname)
print('Age:', My_Resume.age)
print(f'Год рождения {My_Resume.year}')
print('Education:', My_Resume.education)
print('Fav_rog_lang:', My_Resume.fav_rog_lang)


