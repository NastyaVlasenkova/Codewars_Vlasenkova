'''
7 kyu
Name: Simple Fun #3: Late Ride
https://www.codewars.com/kata/588422ba4e8efb583d00007d
Task: Используя таймер велосипеда, рассчитайте текущее время.
Верните ответ в виде суммы цифр, которые будет показывать цифровой таймер в формате hh: mm.
'''

def late_ride(n):
    hours=n//60
    minutes=n-hours*60;
    return hours//10+hours%10+minutes//10+minutes%10