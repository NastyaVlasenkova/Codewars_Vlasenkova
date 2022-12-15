'''
4 kyu
Name:  Breadcrumb Generator
https://www.codewars.com/kata/563fbac924106b8bf7000046
Task: Для этого ката ваша цель - создать функцию, которая принимает URL-адрес,
удаляет первую часть (всегда помечая ее HOME), а затем создает ее, делая каждый элемент, кроме последнего<a>,
элементом, ссылающимся на соответствующий путь; последним должен быть <span>элемент, получающий active class.
'''


ignore=["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
def generate_bc(url, separator):
    temp=[i for i in url.replace("https://", "").replace("http://", "").split("/") if i]
    if temp[-1].startswith("index"):
        temp.pop()
    res=[]
    slash=""
    for i,j in enumerate(temp):
        if i==len(temp)-1:
            index=next((k for k,l in enumerate(j) if not (l.isalnum() or l=="-")), len(j))
            check=j[:index]
            if i==0:
                data="HOME"
            else:
                data=check.replace("-", " ").upper() if len(check)<=30 else "".join(k[0].upper() for k in check.split("-") if k not in ignore)
            res.append("<span class="+'"'+"active"+'"'+">"+data+"</span>")
        elif i==0:
            res.append('<a href="/">HOME</a>')
        else:
            slash+="/"+j
            data=j.replace("-", " ").upper() if len(j)<=30 else "".join(k[0].upper() for k in j.split("-") if k not in ignore)
            res.append("<a href="+'"'+slash+'/"'+">"+data+"</a>")
    return separator.join(res)