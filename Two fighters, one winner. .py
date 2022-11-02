'''
7 kyu
Name: Two fighters, one winner.
https://www.codewars.com/kata/577bd8d4ae2807c64b00045b
Task: Создайте функцию, которая возвращает имя победителя в поединке между двумя бойцами.
'''

def declare_winner(f1, f2, first_attacker):
    position=first_attacker
    while True:
        if position==f1.name:
            f2.health-=f1.damage_per_attack
            if f2.health<=0:
                return position
            position=f2.name
        if position==f2.name:
            f1.health-=f2.damage_per_attack
            if f1.health<=0:
                return position
            position=f1.name