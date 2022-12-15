'''
4 kyu
Name:  Cracking the Vigenère cipher, step 1: determining key length
https://www.codewars.com/kata/55d6afe3423873eabe000069
Task: Напишите функцию, которая принимает некоторый зашифрованный текст и максимально возможную длину ключа
и возвращает длину ключа, который использовался в процессе шифрования.
'''


def get_key_length(cipher_text,max_key_length):
    arr=[0 for x in range(max_key_length-1)]
    for item in range(1,max_key_length):
        num_count=0
        for j in range(len(cipher_text)-(item+1)):
            if cipher_text[j+(item+1)]==cipher_text[j]:
                num_count+=1
        arr[item-1]=num_count
    return arr.index(max(arr))+2