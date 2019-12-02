import random
from tabulate import tabulate
def N_1(l:list,function,p):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                temp = l[:]
                temp[i], temp[j] = temp[j], temp[i]
                if function(temp, p) < function(l, p):
                    l = temp[:]
                    return l
    return l


def N_2(l:list,function,p):
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j:
                temp=l[:]
                v=temp.pop(i)
                temp.insert(j,v)
                if function(temp,p) < function(l,p):
                    l = temp[:]
                    return l
    return l


def N_3(l:list,function,p):
    for i in range(len(l)-2):
        for j in range(i+2,len(l)-1):
            if (j-i)>=3:
                temp=l[0:i+1]+list(reversed(l[i+1:j+1]))+l[j+1:]
                if function(temp, p) < function(l, p):
                    l = temp[:]
                    return l
            return l


def N_4(l:list,function,p):
    for i in range(len(l)-1):
        for j in range(i+2,len(l)-1):
            if i!=j:
                temp=l[:]
                temp[i],temp[i+1],temp[j],temp[j+1]=temp[j],temp[j+1],temp[i],temp[i+1]
                if function(temp, p) < function(l, p):
                    l = temp[:]
                    return l
    return l


def fonction_objective(P: list, m: int):
    result = 0
    c = [0 for _ in range(m)]
    for i in range(0, len(P)):
        result = max(min(c), result) + P[i][0]
        c[c.index(min(c))] = max(result, c[c.index(min(c))]) + P[i][1]
    return result


def N_5(l:list,function,p):
     for i in range(len(l)-5):
        for j in range(i+2,len(l)-3):
            for k in range(j+2,len(l)-1):
                if (j-i)>=3 and (k-j)>=3:
                    temp=l[0:i+1]+l[j+1:k+1]+l[i+1:j+1]+l[k+1:]
                    if function(temp, p) < function(l, p):
                        l = temp[:]
                        return l
     return l


