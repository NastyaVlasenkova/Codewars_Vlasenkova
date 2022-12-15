'''
4 kyu
Name:  Longest Common Subsequence (Performance version)
https://www.codewars.com/kata/593ff8b39e1cc4bae9000070
Task: Напишите функцию lcs, которая принимает две strings и возвращает их
самую длинную общую подпоследовательность как a string.
'''


def lcs(x, y):
    if x=="" or y=="":
        return ""
    arr=[["" for item in range(len(y))] for item in range (len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                if i==0 or j==0:
                    arr[i][j]=x[i]
                else:
                    arr[i][j]=arr[i-1][j-1]+x[i]
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1],key=len)
    return arr[-1][-1]