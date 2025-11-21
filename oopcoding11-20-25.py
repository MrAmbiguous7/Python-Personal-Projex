import random

class RPGclass:
    def __init__(self, name1, weptype, health, mana,):
        self.name1 = name1 
        self.weptype = weptype
        self.health = health
        self.mana = mana
        self.level = 1
    def __str__(self):
        return f"Stats : [ Weapon type: {self.weptype} | Health : {self.health} | Mana : {self.mana} | Lvl : {self.level} | ]"
    def attack(self, target):
        self.target = target
        print(f'{self.name1} attacks {target}')
    def tookdamage(self, dmg):
        self.health -= dmg
        print(f"{self.name1} took {dmg} damage. Current health: {self.health}")
    def checkhealth(self):
        if self.health < 0:
            return f"Dead"
        else:
            return f"{self.health}"
    
class warrior(RPGclass):
    def __init__(self, name1, weptype, health, mana, physdam):
        super().__init__(name1, weptype, health, mana,)
        self.physdam = physdam
class assassin(RPGclass):
    def __init__(self, name1, weptype, health, mana, sneakdam):
        super().__init__(name1, weptype, health, mana)
        self.sneakdam = sneakdam
class mage(RPGclass):
    def __init__(self, name1, weptype, health, mana, magdam):
        super().__init__(name1, weptype, health, mana)
        self.magdam = magdam
class demon_l1(RPGclass):
    def __init__(self, name1, weptype, health, mana, physdam):
        super().__init__(name1, weptype, health, mana)
        self.physdam = 10


character_set_1 = warrior("Brun","Blunt",100,5,20)
character_set_2 = assassin("Helon","Blade",80,10,27)
character_set_3 = mage("SureFire","Wand",60,40,33)

demon_enemy_l1 = demon_l1("Killer", "Blunt", 20, 0, 10)
demon_enemy2_l1 = demon_l1("Ripper", "Blunt",20, 0, 10)

class Event():
    def __init__(self, locationindex):
        self.locationindex = locationindex
        self.LOCATIONS = ['Forest','Castle','Pond','Jungle']
    def __str__(self):
        return f"You walk down the path and you come upon a {self.LOCATIONS[self.locationindex]}\n Then you see two enemies! What do you do?"
    def changeloc(self, locationindex):
        self.locationindex = locationindex
        locationindex += 1
userchoice = input("0 or w to play")
while userchoice == 'w':
    Userset = character_set_1

    print(Userset)
    userevent = Event(0)
    print(userevent)
    userinput = input("1) Attack , 2) Flee")
    if userinput == '1':
        demon_enemy_l1.tookdamage(Userset.physdam)
        print(f"The second demon is at {demon_enemy2_l1.checkhealth()}, and attacks you!")
        Userset.tookdamage(demon_enemy2_l1.physdam)
        break
    else:
        print("You walk away.")
        break
'''
def main():
    try:
        userin = input("What class would you like to play as? (w)arrior , (a)ssassin , (m)age ?  (q) to quit")
        if userin == 'q':
            print("goodbye")
        elif userin == 'w':
            print(character_set_1)
            event = Event(0)
            print(event)
        elif userin == 'a':
            print(character_set_2)
            event = Event(1)
        elif userin == 'm':
            print(character_set_3)
            event = Event(2)

    except ValueError as valerr:
        print("You produced a {valerr} , you should input w,a,m, or q.")
'''

