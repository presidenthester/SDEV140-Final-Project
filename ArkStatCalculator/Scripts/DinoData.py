class Dinos:
    
    def __init__(self, name, health, stamina, oxygen, food, weight, melee, speed, torpor):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.oxygen = oxygen
        self.food = food
        self.weight = weight
        self.melee = melee
        self.speed = speed
        self.torpor = torpor

   

    def fullDino(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.name, self.health, self.stamina, self.oxygen, self.food, self.weight, self.melee, self.speed, self.torpor)

    def healthBump(self):
        return "{}".format(self.health)

    


anky = Dinos("Ankylosaurus", 700, 175, 150, 3000, 250, 100, 100, 420)
bronto = Dinos("Brontosaurus", 2070, 240, 150, 10000, 1600, 100, 100, 2000)
carno = Dinos("Carnotaurus", 420, 300, 150, 2000, 300, 100, 100, 350)
daeodon = Dinos("Daeodon", 900, 250, 150, 2500, 400, 100, 100, 800)
giga = Dinos("Giganotosaurus", 80000, 400, 150, 4000, 700, 100, 100, 10000)
megatherium = Dinos("Megatherium", 740, 400, 270, 3000, 725, 100, 100, 1000)
raptor = Dinos("Raptor", 200, 150, 150, 1200, 140, 100, 100, 180)
rex = Dinos("Rex", 1100, 420, 150, 3000, 500, 100, 100, 1550)
spino = Dinos("Spinosaur", 700, 350, 650, 2600, 350, 100, 100, 850)
theri = Dinos("Therizinosaurus", 870, 300, 150, 3000, 365, 100, 100, 925)
yutu = Dinos("Yutyrannus", 1100, 420, 150, 3000, 500, 100, 100, 1550)


ankyStatBumpPerLevel = Dinos("Ankylosaurus", 140, 17.5, 15, 300, 5, 1.05, 0, 25.2)
brontoStatBumpPerLevel = Dinos("Brontosaurus", 414, 24, 15, 1000, 32, 1.05, 0, 120)
carnoStatBumpPerLevel = Dinos("Carnotaurus", 84, 30, 15, 200, 6, 1.05, 0, 21)
daeodonStatBumpPerLevel = Dinos("Daeodon", 180, 25, 15, 250, 8, 1.05, 0, 48)
gigaStatBumpPerLevel = Dinos("Giganotosaurus", 40, 0.2, 0.375, 10, 7, 1.05, 0, 600)
megatheriumStatBumpPerLevel= Dinos("Megatherium", 148, 40, 27, 300, 14.5, 1.05, 0, 60)
rapotorStatBumpPerLevel = Dinos("Raptor", 40, 15, 15, 120, 2.8, 1.05, 0, 10.8)
rexStatBumpPerLevel = Dinos("Rex", 220, 42, 15, 300, 10, 1.05, 0, 93)
spinoStatBumpPerLevel = Dinos("Spino", 140, 35, 65, 260, 7, 1.05, 0, 51)
theriStatBumpPerLevel = Dinos("Therizinosaurus", 174, 30, 15, 300, 7.3, 1.05, 0, 55.5)
yutuStatBumpPerLevel = Dinos("Yutyrannus", 220, 42, 15, 300, 10, 1.05, 0, 93)

