'''
5 kyu
Name: Linked Lists - Alternating Split
https://www.codewars.com/kata/55dd5386575839a74f0000a9
Task: Напишите функцию AlternatingSplit(), которая принимает один список и разделяет его узлы,
чтобы создать два меньших списка. Подсписки должны быть составлены из чередующихся элементов в исходном списке.
'''


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    output = Context(head, head.next)
    current = head
    while current:
        next = current.next
        current.next = next.next if next else None
        current = next
    return output