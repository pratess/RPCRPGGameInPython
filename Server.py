#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from xmlrpc import server
## Status
MonsterHp= 15
MonsterStamina = 4
Hp = 10
Stamina = 5

## Monster IA
def Monsteraction():
   global MonsterStamina
   if(MonsterStamina == 0):
    return 3
   elif(MonsterStamina > 0 and MonsterStamina <4):
    return random.choice([1, 2])
   else:
    return random.choice([1, 2, 3])

def VerifyStamina():
    global Stamina
    if(Stamina > 0):
        return 0
    else:
        return 1

def VerifyHp():
    global Hp
    if(Hp <= 0):
        return 0
    else:
        return 1

def VerifyMonsterHp():
    global MonsterHp
    if(MonsterHp <= 0):
        return 0
    else:
        return 1

def Fight(DoSomething):
 Monster = Monsteraction()
 Verify = VerifyStamina()
 VerifyHP = VerifyHp()
 VerifyMonsterHP = VerifyMonsterHp()
 global Hp, MonsterHp, Stamina, MonsterStamina
 print("Your Hp: {}".format(Hp))
 print("Your Stamina: {}".format(Stamina))
 print("Monster Hp: {}".format(MonsterHp))
 print("Monster Stamina: {}".format(MonsterStamina))
 if(VerifyHP == 0 and VerifyMonsterHP > 0):
     MonsterHp = 15
     MonsterStamina = 4
     Hp = 10
     Stamina = 5
     return "You Die"

 elif(VerifyHP > 0 and VerifyMonsterHP == 0):
     MonsterHp = 15
     MonsterStamina = 4
     Hp = 10
     Stamina = 5
     return "You Win"

 elif(VerifyHP == 0 and VerifyMonsterHP == 0):
     MonsterHp = 15
     MonsterStamina = 4
     Hp = 10
     Stamina = 5
     return "The two died"

 if(Verify == 0):
    if(DoSomething == 1):
        if(Monster == 1):
            Hp-= 3
            Stamina-= 2
            MonsterHp-= 2
            MonsterStamina-= 2
            return"   O  /\n   \//\n   |/ \n  / \nYou lost 3 Hp and monster lost 2"
        elif(Monster == 2):
            Stamina-= 2
            MonsterStamina-= 1
            return "   O  /\n   \//\n   |/ \n / \nMonster Defends "
        elif(Monster == 3):
            MonsterHp-= 2
            MonsterStamina+= 2
            return "   O  /\n   \//\n   |/ \n / \nMonster lost 2 Hp "
    elif(DoSomething == 2):
        if(Monster == 1):
            Hp-= 3
            MonsterHp-= 4
            Stamina-= 3
            MonsterStamina -= 2
            return "   O\n  / \+--->\n / \ \n/  /\nYou lost 3 Hp and monster lost 4"
        elif (Monster == 2):
            Stamina-= 3
            MonsterStamina-= 1
            return "   O\n  / \+--->\n / \ \n/  /\nMonster Defends"
        elif (Monster == 3):
            MonsterHp-= 4
            Stamina-= 3
            MonsterStamina+= 2
            return "   O\n  / \+--->\n / \ \n/  /\nMonster lost 4 Hp"
    elif(DoSomething == 3):
        if (Monster == 1):
            Stamina -= 1
            MonsterStamina -= 2
            return "   O } \n  / \}\n / \ |\n/  /\nYou defend"
        elif (Monster == 2):
            Stamina -= 1
            MonsterStamina -= 1
            return "   O } \n  / \}\n / \ |\n/  /\nThe Two defended"
        elif (Monster == 3):
            Stamina -= 1
            MonsterStamina += 2
            return "   O } \n  / \}\n / \ |\n/  /\nMonster resting"
    elif(DoSomething == 4):
        if (Monster == 1):
            Hp -= 3
            Stamina += 5
            MonsterStamina -= 2
            return "   O\n   \/\n   | \n  / \ \nYou lost 3 hp and recover stamina"
        elif (Monster == 2):
            Stamina += 5
            MonsterStamina -= 1
            return "   O\n   \/\n   | \n  / \ \nMonster defends and you recover stamina"
        elif (Monster == 3):
            Stamina += 5
            MonsterStamina += 2
            return "   O\n   \/\n   | \n  / \ \nThe two resting"
 else:
     if (Monster == 1):
         Hp -= 3
         Stamina += 5
         MonsterStamina -= 2
         return "   O\n   \/\n   | \n  / \ \nYou lost 3 hp and recover stamina"
     elif (Monster == 2):
         Stamina += 5
         MonsterStamina -= 1
         return "   O\n   \/\n   | \n  / \ \nMonster defends and you recover stamina"
     elif (Monster == 3):
         Stamina += 5
         MonsterStamina += 2
         return "   O\n   \/\n   | \n  / \ \nThe two resting"


def TheUltimateNonsenseFight2017PythonVersion() :

        return "The Ultimate Nonsense Fight 2017\n      Python Edition\n   ( <O  O>  )\n  {(   \/    )}\n  {(  ----   )]\n  { \       /}\n      \   /\n\n\n\n"



def main():

    Server = server.SimpleXMLRPCServer(("localhost", 8000))
    print ("Listening on port 8000...")

    Server.register_function(TheUltimateNonsenseFight2017PythonVersion, 'Game')
    Server.register_function(Fight, 'Fight')

    Server.serve_forever()

if __name__ == "__main__":
    main()
