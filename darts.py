import random
def igra (L,K,t1,t2):
    chek = 0
    print('Первое попадание = ',t1)
    print('Второе попадание = ',t2)
    print('Номер сектора первого дротика = ',L.index(t1))
    print('номер сектора второго дротика = ',L.index(t2))
    if L.index(t1) > L.index(t2):
        if (K >= t2) and (K <= t1):
            h = False
        else:
            h = True
        i = L.index(t1)
        if h ==True :
            while i < len(L):
                chek = chek+L[i]
                i = i+1
            i = 0
            while i <= L.index(t2):
                chek = chek + L[i]
                i = i + 1
    elif L.index(t1) < L.index(t2):
        i=L.index(t1)
        while i <= L.index(t2):
            if i == K:
                chek = 0
                break
            chek = chek+L[i]
            i = i+1
    elif L.index(t1) == L.index(t2):
        chek = t1
    return chek

def Max(K,L):
    if K == -1:
        sum=0
        for i in range(len(L)):
            sum1=0
            L2=L[i+1:]+L[:i+1]
            for j in range(len(L2)):
                ans2=L2[0]
                sum1+=L2[j]
                ans2=max(ans2,sum1)
                sum1=max(sum1,0)
            sum=max(sum,sum1)

    else:
        sum=0
        L1 = L[K + 1:] + L[:K]
        ans1=L1[0]
        print(L1)
        for o in range(len(L1)):
            sum+=L1[o]
            ans1=max(ans1,sum)
            sum=max(sum,0)

    return sum

x=int(input('Введите количсетво играков = '))
i=0
N = int(input('Введите количество секторов = '))
K=int(input('Введите номер черного сектора = '))
L = list(map(int, input().split()))
while i<x:
    t1 = random.choice(L)
    t2 = random.choice(L)
    if i == 0:
        print('Максимальная сумма = ',Max(K,L))
    print('Игрок  '+str(i+1)+' заработал = ',igra(L,K,t1,t2))
    i=i+1
