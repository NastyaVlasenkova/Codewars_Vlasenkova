'''
4 kyu
Name:  Simple maze
https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c
Task: Для данного лабиринта и положения Кейт найдите, есть ли выход. Ваша функция должна возвращать True или False .
'''


from queue import PriorityQueue
moves=[(0,1),(0,-1),(-1,0),(1,0)]

def has_exit(maze):
    if sum(j=="k" for i in maze for j in i)!=1:
        raise Exception()
    result=PriorityQueue()
    start=next((i, k) for i,j in enumerate(maze) for k,l in enumerate(j) if l=="k")
    result.put((0,(start[0],start[1])))
    edge=[0,len(maze)-1,0,len(maze[0])-1]
    memo=set()
    while not result.empty():
        location=result.get()
        if location[1][0] in edge[:2] or location[1][1] in edge[2:]:
            return True
        elif location[1] in memo:
            continue
        memo.add(location[1])
        for i,j in moves:
            y,x =location[1][0]+i, location[1][1]+j
            if (0<=y<=edge[1] and 0<=x<=edge[3]) and maze[y][x]==" ":
                result.put((location[0]+1,(y,x)))
    return False