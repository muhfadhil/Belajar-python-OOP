class Hero():

    def __init__(self, name):
        self.health_pool = [0,100,150,200,250]
        self.attack_pool = [0,10,15,20,25]
        self.armor_pool = [0,5,10,20,40]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print("{}: \n\thealth :{} \n\tattack :{} \n\tarmor :{}".format(
            self.__name,
            self.__health,
            self.__attack,
            self.__armor
            )
        )

    @property
    def health_pool(self):
        pass

    @property
    def attack_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def gainExp(self):
        pass

    @property
    def levelUp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input

    @attack_pool.setter
    def attack_pool(self,input):
        self.__attack_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attack = self.__attack_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.levelUp = self.__exp // 100
            self.__exp %= 100


class HeroIntelligent(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,100,200,300,400]
        self.attack_pool = [0,10,20,30,40]
        self.armor_pool = [0,3,6,9,12]
        self.__level = 1


class HeroStrenght(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,150,250,350,450]
        self.attack_pool = [0,5,25,35,45]
        self.armor_pool = [0,10,20,30,40]
        self.__level = 1


liukang = HeroIntelligent('liukang')
kunglau = HeroStrenght('kunglau')

liukang.gainExp = 200
kunglau.gainExp = 250

liukang.show_info()
kunglau.show_info()
