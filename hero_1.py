import random
class Unit:
    def __init__(self, name, damage, health, armour, iniative, posX, posY, speed,  range):
        self.damage = damage
        self.health = health
        self.armour = armour
        self.iniative = iniative
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.name = name
        self.range = range
        self.alive = True
    def getDamage(self, damage):
        if(self.health + self.armour < damage):
            self.health =  0
        else:
            self.health =  self.health +self.armour - damage

    def stepUp(self):
        self.posY+=self.speed

    def stepDown(self):
        self.posY-=self.speed

    def stepRight(self):
        self.posX+=self.speed

    def stepLeft(self):
        self.posX-=self.speed

    def attack(self, damagedUnit):
        damagedUnit.getDamage(self.damage)

    def getPosition(self):
        return [self.posY, self.posX]

    def canAttack(self, pavuk):
        if( self.posX == pavuk.posX and (abs(self.posY - pavuk.posY) <= self.range ) and pavuk.alive == True):
            return True
        if( self.posY == pavuk.posY and (abs(self.posX - pavuk.posX) <= self.range ) and pavuk.alive == True):
            return True
        return False

    def move(self, command):
        if(command == "w"):
            self.stepUp()
        if(command == "s"):
            self.stepDown()
        if(command == "a"):
            self.stepLeft()
        if(command == "d"):
            self.stepRight()

        if(self.posX>50):
            self.posX =50
        if(self.posX < -50):
            self.posX = -50

        if(self.posY>50):
            self.posY = 50
        if(self.posY < -50):
            self.posY = -50
        self.iniative= random.randrange(1,21)+self.iniative

class MonsterPavuk(Unit):
    def __init__(self, name, posX, posY):
        health = 15
        armour = 0
        speed = 5
        damage = 5
        iniative = 1
        self.alive = True

        super().__init__(name,  damage, health, armour, iniative, posX, posY, speed, 5)




Khlamkin=Unit("Хламкин", 11, 50, 0, 5, 0, 0, 5, 10)
Pavuki = [MonsterPavuk("Вася", 0, 15), MonsterPavuk("Петя", 15, 15), MonsterPavuk("Обэма", 25, 15)]


Pavuki[0].attack(Khlamkin)
print(Khlamkin.health)


# ПАВУК БРОДИТw
for Pavuk in Pavuki:
    rand = random.randrange(0,5)
    if(rand == 1 ):
        Pavuk.stepUp()
    elif(rand == 2):
       Pavuk.stepDown()
    elif(rand == 3):
        Pavuk.stepLeft()
    elif(rand == 4):
       Pavuk.stepRight()
    print("Павук ", Pavuk.name, " На", Pavuk.getPosition(), "\n")

resume = ""
while(resume !="q"):
    #ГЕРОЙ ПОШОЛ АСЮДАВА
    print("Куда идем, старина ", Khlamkin.name,"?\n")
    command = input()
    Khlamkin.move(command)

    print("Приветсвую тебя в ", Khlamkin.getPosition(),"\n")
    canAttackedPavuks = []

    for Pavuk in Pavuki:
        if(Khlamkin.canAttack(Pavuk)):
            canAttackedPavuks.append(Pavuk)
    if(len(canAttackedPavuks) == 0):
        print("Ты не можешь ничего скотина скучная никто тебя не любит:")
    else:
        print("Вы можете атаковать следующих павуков:")

    i = 0
    for canAttackedPavuk in canAttackedPavuks:
        print(i, " ", canAttackedPavuk.name, "\n")
        i+=1
    newCommnad = input("Введите павука, x для выхода или команду движение:\n")
    if(newCommnad == "w" or newCommnad =="a" or newCommnad =="s" or newCommnad =="d" or newCommnad =="x"):
        Khlamkin.move(newCommnad)
        print("Хламкин  бежал на клетку ",Khlamkin.getPosition())
    if(newCommnad == "0" or newCommnad == "1" or newCommnad =="2" or newCommnad =="3" or newCommnad =="4"):
         if(Khlamkin.iniative > canAttackedPavuks[int(newCommnad)].iniative):
            Khlamkin.attack(canAttackedPavuks[int(newCommnad)])
            if(canAttackedPavuks[int(newCommnad)].health < 1):
                print(canAttackedPavuks[int(newCommnad)].name, "пал смертью для салата помянем!")
                canAttackedPavuks[int(newCommnad)].alive = False
            else:
                if(canAttackedPavuks[int(newCommnad)].canAttack(Khlamkin)):
                    canAttackedPavuks[int(newCommnad)].attack(Khlamkin)
                    if(Khlamkin.health < 1):
                        resume = "q"
                        print(Khlamkin.name, " жил без страха, и умер без страха\n поделом\n проклятые братья бури \n в скайриме было спокойно пока вы не явились\n помянем, здоровья погибшим")
                print("Здоровье павука ", canAttackedPavuks[int(newCommnad)].name, ": ", canAttackedPavuks[int(newCommnad)].health)
         else: #dfszd
            canAttackedPavuks[int(newCommnad)].attack(Khlamkin)
            if(canAttackedPavuks[int(newCommnad)].health < 1):
                print(canAttackedPavuks[int(newCommnad)].name, "пал смертью для салата помянем!")
                canAttackedPavuks[int(newCommnad)].alive = False
            else:
                if(Khlamkin.canAttack(canAttackedPavuks[int(newCommnad)])):
                    Khlamkin.attack(canAttackedPavuks[int(newCommnad)])
                    if(Khlamkin.health < 1):
                        resume = "q"
                        print(Khlamkin.name, " жил без страха, и умер без страха\n поделом\n проклятые братья бури \n в скайриме было спокойно пока вы не явились\n помянем, здоровья погибшим")
                print("Здоровье павука ", canAttackedPavuks[int(newCommnad)].name, ": ", canAttackedPavuks[int(newCommnad)].health)
    if(resume != "q"):
        resume = input("Введите q для выхода")