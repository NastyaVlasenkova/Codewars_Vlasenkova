'''
4 kyu
Name: Sort binary tree by levels
https://www.codewars.com/kata/5324945e2ece5e1f32000370/solutions/python
Task: Ваша задача - вернуть список с элементами из дерева, отсортированными по уровням, что означает,
что корневой элемент идет первым, затем корневые дочерние элементы (слева направо)
являются вторыми и третьими, и так далее.
Возвращает пустой список, если есть root None.
'''


from collections import deque
def tree_by_levels(node):
    if not node:
        return []
    arr=deque([node])
    result=[]
    while arr:
        result.append(arr[-1].value)
        if arr[-1].left:
            arr.appendleft(arr[-1].left)
        if arr[-1].right:
            arr.appendleft(arr[-1].right)
        arr.pop()
    return result