'''
4 kyu
Name:  Strings Mix
https://www.codewars.com/kata/5629db57620258aa9d000014
Task: Учитывая две строки s1 и s2, мы хотим представить, насколько различны эти две строки.
Мы будем учитывать только строчные буквы (от a до z).
Задача состоит в том, чтобы создать строку, в которой каждая строчная буква s1 или s2 появляется столько раз,
сколько ее максимум, если этот максимум строго больше 1;
'''


from collections import Counter
def mix(s1,s2):
    result1=Counter([i for i in s1 if i.islower()])
    result2=Counter([i for i in s2 if i.islower()])
    final=[]
    for i in "abcdefghijklmnopqrstuvwxyz":
        if result1.get(i,0)>result2.get(i,1):
            final.append("1:"+i*result1[i])
        elif result2.get(i,0)>result1.get(i,1):
            final.append("2:"+i*result2[i])
        elif result1.get(i,0)==result2.get(i,-1)and result1.get(i, 0)>=2:
            final.append("=:"+i*result1[i])
    final.sort()
    final.sort(key=len, reverse=True)
    return "/".join(final)