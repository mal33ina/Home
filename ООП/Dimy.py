import datetime

def time():
    today = datetime.datetime.today()
    return today.strftime("%Y")

class Resume:
    def __init__(self, obgname, objage, obj_fav_prog_lang, objexperience):
        self.name = obgname
        self.age = objage
        self.fav_prog_lang = obj_fav_prog_lang
        self.experience = objexperience
        self.year = int(time()) - self.age




me = Resume('Dzmitry', 26, 'Python', 'two months')

print(f'Имя:{me.name}')
print(f'Возраст:{me.age}')
print(f'любимый язык программирования:{me.fav_prog_lang}')
print(f'опыт работы:{me.experience}')
print(me.year)
