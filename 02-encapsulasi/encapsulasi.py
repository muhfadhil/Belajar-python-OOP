class Hero():
    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__healthBase = health
        self.__attackBase = attack
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attack = self.__attackBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax
        Hero.__jumlah += 1

    @property
    def info(self):
        return '{} : \n\thealth :{}/{} \n\tattack :{} \n\tarmor  :{}'.format(self.__name,self.__health,self.__healthMax,self.__attack,self.__armor)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, inputExp):
        self.__exp += inputExp
        if (self.__exp >= 100):
            self.__level += 1
            print('level', str(self.__level)+',', self.__name,'level up')
            self.__exp -= 100
            
            self.__healthMax = self.__healthBase * self.__level
            self.__attack = self.__attackBase * self.__level
            self.__armor = self.__armorBase * self.__level

    def serang(self, musuh):
        print(self.__name,'menyerang',musuh.__name)
        self.gainExp = 40
        musuh.diserang(self)
        
    def diserang(self, musuh):
        print(self.__name,'diserang',musuh.__name)
        self.__health -= musuh.__attack

    @property
    def health(self):
        pass

    @health.getter
    def health(self):
        return self.__health



kunglau = Hero('Kunglau', 100, 20, 10)
liukang = Hero('Liukang', 100, 30, 10)

"""
kunglau.serang(liukang)
kunglau.serang(liukang)
kunglau.serang(liukang)
"""

while True:
    kunglau.serang(liukang)
    liukang.serang(kunglau)

    if kunglau.health <=0:
        print("KUNGLAU DEAD")
        break
    
    if liukang.health <= 0:
        print('LIUKANG DEAD')
        break

print(kunglau.info)
print(liukang.info)