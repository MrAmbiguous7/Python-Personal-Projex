import random

WeptypeDict = {"Blunt": .06, "Blade": .08, "Wand": .03}
DamageSetsClass_p = {"Warrior":random.randint(20,31), "Assassin":random.randint(20,27), "Mage" : random.randint(22,35)}
BaseClassNums = {"Warrior": ["Brun", "Blunt", 100, 5], "Assassin": ["Heron", "Blade", 75, 15], "Mage": ["SureFire", "Wand", 60, 50]}
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
    def calculatedamagetaken(self, sweptype, tweptype, tlevel, location, in_dam):
        if sweptype == "Blunt" and tweptype == "Blade":
            dmg = (WeptypeDict["Blade"] * 100) + in_dam + ((tlevel-1) * 5)
            if location == "Castle":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Blunt" and tweptype == "Blunt":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Castle":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Blunt" and tweptype == "Wand":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Castle":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Blade" and tweptype == "Wand":
            dmg = (WeptypeDict["Wand"] * 100) + in_dam + ((tlevel-1) * 5)
            if location == "Forest":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Blade" and tweptype == "Blade":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Forest":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Blade" and tweptype == "Blunt":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Forest":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Wand" and tweptype == "Blunt":
            dmg = (WeptypeDict["Blade"] * 100) + in_dam + ((tlevel-1) * 5)
            if location == "Pond":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Wand" and tweptype == "Wand":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Pond":
                dmg -= 9 - (tlevel)
            return dmg
        elif sweptype == "Wand" and tweptype == "Blade":
            dmg = in_dam + ((tlevel-1) * 5)
            if location == "Pond":
                dmg -= 9 - (tlevel)
            return dmg
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
        super().__init__(name1, weptype, health, mana)
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


'''
Need to add: algorithm to change damage values based on weapon type
Need to add: logic to determine how much each person's damage is based on type and target
Need to add: misc other things -- will add as I go... will also be writing comments for the code soon

'''


class Event():
    def __init__(self, locationindex):
        self.locationindex = locationindex
        self.LOCATIONS = ['Pond','Forest','Castle',]
    def __str__(self):
        return f"You walk down the path and you come upon a {self.LOCATIONS[self.locationindex]}\n Then you see two enemies! What do you do?"
    def changeloc(self, locationindex):
        self.locationindex = locationindex
        locationindex += 1
        if locationindex == 3:
            locationindex = 0
            '''
ftest1 = BaseClassNums["Warrior"]
test1 = warrior(*ftest1, DamageSetsClass_p["Warrior"])
print(test1.physdam)
print(test1)
'''
war_i = BaseClassNums["Warrior"]
war_c = warrior(BaseClassNums["Warrior"], DamageSetsClass_p["Warrior"]) 
as_i = BaseClassNums["Assassin"]
as_c = assassin(BaseClassNums["Assassn"], DamageSetsClass_p["Assassin"])
mag_i = BaseClassNums["Mage"]
mag_c = mage(BaseClassNums["Mage"], DamageSetsClass_p["Mage"])
userchoicelist = ["w"."a","m"]
userchoice = input("q to quit, w for warrior, a for assassin, m for mage")
while userchoice == "w" or "a" or "m":
    if userchoice ==  "w":

        userset = 





'''
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

