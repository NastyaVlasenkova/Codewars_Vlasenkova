'''
6 kyu
Name: Linked Lists - Length & Count
https://www.codewars.com/kata/55beec7dd347078289000021
Task: Реализуйте функцию Length() для подсчета количества узлов в связанном списке.
Реализуйте функцию Count() для подсчета вхождений целого числа в связанный список.
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if not node:
        return 0
    length = 1
    while node.next:
        node = node.next
        length += 1
    return length


def count(node, data):
    if not node:
        return 0
    count = 0
    while node:
        if node.data == data:
            count += 1
        node = node.next
    return count