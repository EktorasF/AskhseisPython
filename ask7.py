import datetime
import urllib.request
import json
url1="https://api.opap.gr/draws/v3.0/1100/draw-date/"
x = datetime.datetime.now()
y=(x.strftime("%Y"))
m=(x.strftime("%m"))
d=(x.strftime("%d"))
day=int(d)
while day > 0:
    d=str(day)
    if day<10:
        d="0"+str(day)
    hmer=y+"-"+m+"-"+d
    url2=url1+hmer+"/"+hmer+"/"+"draw-id"
    r=urllib.request.urlopen(url2)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    url3="https://api.opap.gr/draws/v3.0/1100/"
    x=0
    lista=[]
    for i in data:
        i=str(i)
        url4=url3+i
        r=urllib.request.urlopen(url4)
        html=r.read()
        html=html.decode()
        data=json.loads(html,strict=False)
        lista.append(data["winningNumbers"]["list"])
        x=x+1
    numbers=[]
    for i in range(80):
        numbers.append(i+1)
    empty=[]
    for i in range(80):
        empty.append(0)
    po=0
    arith_klhr=x-1
    while po < arith_klhr:
        for k in lista[po]:
            for j in numbers:
                if j==k:
                    empty[j-1]=empty[j-1]+1
        po=po+1
    print(empty.index(max(empty))+1,":", (max(empty)), "φορές εμφανίστηκε την ημέρα",hmer)
    day=day-1
