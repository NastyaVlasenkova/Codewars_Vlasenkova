'''
4 kyu
Name:  Factorial tail
https://www.codewars.com/kata/55c4eb777e07c13528000021
Task: заключается в том, чтобы написать функцию, которая найдет количество нулей
в конце (number)факториала в произвольном основании = base для больших чисел.
'''


def zeroes(base, number):
    temp=factorization(base)
    result=float("inf")
    for i,j in temp.items():
        num=number
        total=0
        key=i
        while num>=key:
            total+=num//key
            num//=key
        result=min(total//j,result)
    return result
def factorization(n):
    result={}
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            n//=factor
            result[factor]=result.get(factor,0)+1
            factor=2
        else:
            factor+=1
    result[n]=result.get(n,0)+1
    return result