SANPAI=1
YIDUI=2
ERDUI=3
LIANDUI=4
SANTIAO=5
SHUNZI=6
TONGHUA=7
HULU=8
ZHADAN=9
TONGHUASHUN=10
P=0.05

def is_same_flower(list):
    flag=True
    if len(list)==3:
        return 0
    else:
        for i in range(1, 5):
            if list[0][0] != list[i][0]:
                flag = False
                break
        if flag:
            return TONGHUA + int(list[4][1:]) * P
        else:
            return 0

def is_shunzi(list):
    if len(list)==3:
        return 0
    else:
        flag = True
        for i in range(1, 5):
            if int(list[i][1:]) - 1 != int(list[i - 1][1:]):
                flag = False
        if flag:
            return SHUNZI + int(list[4][1:]) * P
        else:
            return 0

def is_zhadan(list):
    flag = True
    if len(list)==3:
        return 0
    else:
        if list[1][1:] != list[2][1:] or list[1][1:] != list[3][1:]:
            flag = False
        if list[1][1:] != list[0][1:] and list[4][1:] != list[3][1:]:
            flag = False
        if flag:
            return ZHADAN + int(list[2][1:]) * P
        else:
            return 0

def is_hulu(list):
    flag = True
    if len(list)==3:
        return 0
    else:
        if list[0][1:]!=list[1][1:] or list[3][1:]!=list[4][1:]:
            flag=False
        if list[3][1:]!=list[2][1:] and list[1][1:]!=list[2][1:]:
            flag=False
        if flag:
            return HULU+int(list[2][1:])*P
        else:
            return 0
def is_santiao(list):
    flag=False
    if list[0][1:]==list[1][1:] and list[0][1:]==list[2][1:]:
        return SANTIAO+int(list[2][1:])*P
    elif len(list)==5:
        for i in range(0,3):
            if list[i][1:] == list[i+1][1:] and list[i][1:] == list[i+2][1:]:
                flag=True
                break
        if flag:
            return SANTIAO+int(list[2][1:])*P
        else:
            return 0
    else:
        return 0

def select_duizi(list):
    if len(list)==3:
        if list[0][1:]==list[1][1:] or list[2][1:]==list[1][1:]:
            return YIDUI+int(list[1][1:])*P
        else:
            return SANPAI+int(list[2][1:])*P
    elif len(list)==5:
        tmp=[]
        i=0
        while i<4:
            if list[i][1:]==list[i+1][1:]:
                tmp.append(i)
                i+=1
            i+=1
        if len(tmp)==1:
            return YIDUI+int(list[tmp[0]][1:])*P
        elif len(tmp)==2:
            if tmp[1]-tmp[0]==2 and int(list[tmp[1]][1:])-int(list[tmp[0]][1:])==1:
                return LIANDUI+int(list[tmp[1]][1:])*P
            else:
                return ERDUI+int(list[tmp[1]][1:])*P
        elif len(tmp)==0:
            return SANPAI+int(list[4][1:])*P


def sort_cards(list):
    cards=[list[10:13],list[5:10],list[0:5]]
    scores=[0,0,0]
    for i in range(0,3):
        if is_same_flower(cards[i])==0:
            scores[i]=is_zhadan(cards[i])
            if scores[i]!=0:
                continue
            scores[i] = is_hulu(cards[i])
            if scores[i] != 0:
                continue
            scores[i] = is_shunzi(cards[i])
            if scores[i] != 0:
                continue
            scores[i] = is_santiao(cards[i])
            if scores[i] != 0:
                continue
            scores[i]=select_duizi(cards[i])
        else:
            scores[i]=is_same_flower(cards[i])
            if is_shunzi(cards[i])!=0:
                scores[i]+=3
    if scores[0]>scores[1] or scores[1]>scores[2]:
        return [0,0,0]
    else:
        return scores

def is_continue(list):
    score=0
    if is_same_flower(list) == 0:
        score= is_zhadan(list)
        if score == 0:
            score = is_hulu(list)
        if score == 0:
            scores = is_shunzi(list)
        if score == 0:
            score = is_santiao(list)
        if score == 0:
            score = select_duizi(list)
    else:
        score = is_same_flower(list)
    if score>3:
        return True
    else:
        return False

if __name__=='__main__':
    #list=['$7', '*8', '$9', '*10', '&11','#4', '&5', '#5', '#11', '*14','&2', '$2', '*2']
    #print(sort_cards(list))
    print(is_santiao(['#4', '&5', '#5', '#11', '*14']))
