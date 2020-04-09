import random
import sys

def qsort(li):
    if len(li)<=1: return li
    pivot=li[len(li)//2]
    down, up, sa =[], [], []
    for i in li:
        if int(i) < int(pivot): down.append(i)
        if int(i) > int(pivot): up.append(i)
        if int(i) == int(pivot): sa.append(i)
    if li == qsort(down)+qsort(sa)+qsort(up) : return li
    return qsort(down)+qsort(sa)+qsort(up)  #int 안해도 되나요?




n=int(input("몇 개의 숫자를 넣으시겠습니까?:"))
box=list(range(1,n+1))
random.shuffle(box)
print("정렬 전 배열:  ",box)


ans=None
while True :
    ans= input(
    "어떤 정렬을 사용하시겠습니까?\n"
    "1: 파이썬에서 제공하는 sort\n"
    "2: bubble sort\n"
    "3: quick sort\n"
    "4: 종료\n"
    )

    if ans=='1':
        box.sort()

    elif ans=='2' :
        for i in range(1,n-1):
            p=n-i
            for h in range(p):
                if box[h] >= box[h+1]: box[h+1], box[h] = box[h], box[h+1]

    elif ans =='3':
        box = qsort(box)

    elif ans =='4':
        print("종료")
        sys.exit(0)

    else:print("잘못된 입력!")

    print("정렬 후 배열:" , box)
