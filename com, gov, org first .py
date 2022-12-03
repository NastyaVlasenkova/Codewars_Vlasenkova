'''
6 kyu
Name: "com", "gov", "org" first
https://www.codewars.com/kata/57f21fcd69e09cb0d2000088
Task: Напишите код, который упорядочивает сбор Uri на основе своего домена следующим образом,
чтобы он возвращал fisrt Uri с доменом "com", "gov", "org" (в алфавитном порядке их доменов),
а затем все остальные Uri, упорядоченные в алфавитном порядке их доменов
'''


def order_by_domain(addresses):
    return sorted(addresses, key= lambda x: (domain(x.split("/")[2].split(".")[-1]), x.split("/")[2].split(".")[-1]))
def domain(s):
    if s=="com":
        return 0
    elif s=="gov":
        return 1
    elif s=="org":
        return 2
    return 3