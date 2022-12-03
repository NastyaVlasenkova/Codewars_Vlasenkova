'''
6 kyu
Name: Complete The Pattern #11 - Plus
https://www.codewars.com/kata/5589ad588ee1db3f5e00005a
Task: Вы должны написать функцию pattern, которая возвращает следующий шаблон до (3n-2) строк, где n - параметр.
'''


def pattern(n):
    if n<=0: return ""
    string="".join([str(i%10) for i in range(1,n)])
    res=""
    for i in range(n-1):
        res+=" "*(n-1)+str((i+1)%10)*n+" "*(n-1)+"\n"
    for i in range(n):
        res+=string+str(n%10)*n+string[::-1]+"\n"
    for i in range(n-1,0,-1):
        res+=" "*(n-1)+str(i%10)*n+" "*(n-1)+"\n"
    return res [:-1]