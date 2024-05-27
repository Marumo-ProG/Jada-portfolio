
'''
    this is a demonstrate of Classes and objects with inheritance in python, here we created a simple
    simulation of a fight between  warriors and a dragon, the warrior has a health level of 400 and the dragon
    where we created 2 classes of the warrios and the dragon and the hero class as the parent class
    and used them to create the objects in our game and simulate the fight between them
'''

from random import randint
class Hero():
   #class constructor
    def __init__(self, name, health, armor):
       self.name = name
       self.health = health #number
       self.armor = armor #string
   #print character parameters:
    def print_info(self):
        print("Name:", self.name)
        print('Health level:', self.health, ":red_heart:")
        print('Armor class:', self.armor, '\n')
    def get_health(self):
        return self.health

class Warrior(Hero):
    def hello(self):
        print('-> NEW HERO! A skilled warrior appears from the forest depths ', self.name )
        
    #method for displaying a text description of the attack on the screen
    def attack(self, enemy): 
        print(self.name , 'attacks fearlessly', enemy.name, ":collision:" )
        enemy.health = enemy.health - 20
        print('The fight outcome for', self.name )
        self.print_info()
        print('The fight outcome for', enemy.name )
        enemy.print_info()

class Dragon(Hero):
    def roar(self):
        print("ROOAAARRRR :fire:")
    def attack(self, enemy):
        print(self.name, "breaths fire :fire: :fire: onto", enemy.name)
        enemy.health = enemy.health - 30
        print("The fight outcome for", self.name)
        self.print_info()
        print("the fight outcome for", enemy.name)
        enemy.print_info()
    

hero_list = [Warrior("Lenny", 400, "iron"),Warrior("Jada", 400, "iron")]
enemy_list = [Warrior("Venom", 150, "none"), Warrior("Thanos", 200, "Magic Hand"), Dragon("King", 400, "Dragon Skin")]


# fight
while len(enemy_list) > 0 and len(hero_list) > 0:
    rand = randint(0,1)
    if rand == 0:
        attack_who = randint(0,len(enemy_list) -1)
        whos_attacking = randint(0,len(hero_list) -1)
        hero_list[whos_attacking].attack(enemy_list[attack_who])
        if enemy_list[attack_who].get_health() < 0:
            del enemy_list[attack_who]
    else:
        whos_attacking = randint(0,len(enemy_list)-1)
        attack_who = randint(0,len(hero_list) -1 )
        enemy_list[whos_attacking].attack(hero_list[attack_who])
        if hero_list[attack_who].get_health() < 0:
            del hero_list[attack_who]

print("Winners :fire: :fire:")
if len(enemy_list) > 0 :
    for enemy in enemy_list:
        enemy.print_info()
else:
    for hero in hero_list:
        hero.print_info()



