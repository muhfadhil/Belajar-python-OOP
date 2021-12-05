class karakter():
    jumlah = 0

    def __init__(self, name, health, attack, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        karakter.jumlah += 1
    
    def tembak(self, musuh):
        print(self.name,'menembak', musuh.name)
        musuh.tertembak(self, self.attack)
    
    def tertembak(self, musuh, damage):
        print(self.name, 'tertembak oleh', musuh.name,'menggunakan',musuh.weapon)
        print(self.name,'terkena', damage,'damage')
        self.health -= damage
        print('sisa darah', self.name,'sebesar',self.health)



victor = karakter("victor", 100, 25, 'm4')
noob = karakter('noob', 100, 20, 'm16')

#victor.tembak(noob)

while True:
    victor.tembak(noob)
    noob.tembak(victor)

    if victor.health <= 0:
        print("VICTOR MATI, NOOB MENANG")
        break
    elif noob.health <= 0:
        print("NOOB MATI, VICTOR MENANG") 
        break
