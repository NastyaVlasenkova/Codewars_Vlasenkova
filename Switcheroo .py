'''
7 kyu
Name: Switcheroo
https://www.codewars.com/kata/57f759bb664021a30300007d
Task: Учитывая строку, состоящую из букв a, b и / или c,
измените положение букв a и b (измените a на b и наоборот).
Оставьте все случаи использования c нетронутыми.
'''

def switcheroo(s):
    result=''
    for item in s:
        if item=='a':
            result+='b'
        elif item=='b':
            result+='a'
        else:
            result+=item
    return result