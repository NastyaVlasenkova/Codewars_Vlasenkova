'''
5 kyu
Name: Domain name validator
https://www.codewars.com/kata/5893933e1a88084be10001a3
Task: В этом ката вам необходимо создать средство проверки доменных имен, в основном совместимое
с RFC 1035, RFC 1123 и RFC 2181
'''


def validate(d):
    a = 1
    while True:
        if (len(d) > 253) or (d.find('.') == -1):
            a = 0
            break
        u = d.split('.')
        if len(u) > 127:
            a = 0
            break
        for i in range(len(u)):
            if (len(u[i]) > 63) or (len(u[i]) < 1) or (u[i][0] == '-') or (u[i][-1] == '-') or (
                    u[-1].isdigit() == True):
                a = 0
                break
            for j in range(len(u[i])):
                if (ord(u[i][j]) < 48) or (ord(u[i][j]) > 57):
                    if (ord(u[i][j]) < 65) or (ord(u[i][j]) > 90):
                        if (ord(u[i][j]) < 97) or (ord(u[i][j]) > 122):
                            if (ord(u[i][j]) != 45):
                                a = 0
                                break

        break
    if a != 0:
        return True
    else:
        return False