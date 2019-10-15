import random

def contains(listx, x):
    flag=False
    for y in listx:
        if(x==y):
            flag=True
            break
    return flag

def deal_cards():
    listx=[]
    while True:
        x = random.randint(0, 51)
        while contains(listx,x):
            x = random.randint(0, 51)
        listx+=[x]
        if len(listx)==13:
            break
    typex=['$','&','*','#']
    list2=[]
    for i in range(0,13):
        y=listx[i]%13+1
        if y==1:
            y= 'A'
        elif y==11:
            y='J'
        elif y==12:
            y='Q'
        elif y==13:
            y='K'
        else:
            y=str(y)
        list2.append(typex[int(listx[i]/13)]+y)
    return list2

def main():
    listx=deal_cards()
    print(listx)

if __name__=='__main__':
    main()
