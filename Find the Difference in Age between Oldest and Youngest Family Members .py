'''
8 kyu
Name: Find the Difference in Age between Oldest and Youngest Family Members
https://www.codewars.com/kata/5720a1cb65a504fdff0003e2
Task: На ежегодном семейном собрании семья любит определять возраст самого старшего из живущих членов семьи
и возраст самого младшего члена семьи и вычислять разницу между ними.
'''

def difference_in_ages(ages):
    return (min(ages),max(ages),max(ages)-min(ages))