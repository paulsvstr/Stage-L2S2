from math import sqrt

vect = open('/home/psevestre/glove.6B.50d.txt','r')

lines = vect.readlines()
dico = {}
cpt = 0
for k in range(0,400000):
    C,L,D = [],[],[]
    L=lines[k]
    D = L.replace("\n","")
    #V = D.replace(",","")
    C = D.split(" ")
    dico[C[0]] = C[1:]
    cpt +=1

print('ok')

def find_center(L) : 
    W , center = [],[]
    for mot in L :
        W.append(dico[mot])
    l = len(W)
    for j in range(50) :
        s = 0
        m = 0
        for mot in W :
            s += float(mot[j])
        m = s/l
        center.append(m)
    return center

L = ['espagne','france','allemagne','italie','angleterre']
L2 = ['vie','vie','vie']
L3 = ['cambridge','oxford']
L4 = ['piano','guitar','instruments']

def ed(u,v) :
    s = 0
    for i in range(50):
        un,vn = float(u[i]),float(v[i])
        s += (un-vn)**2
    return sqrt(s)

def MPP(L,dic) :
    c = find_center(L)
    dmin = ed(dic['the'],c)
    mpp = ""
    cpt = 0
    for vec in dic :
        d = ed(dic[vec],c)
        cpt +=1
        if cpt%100000 == 0:
            print(cpt,'/400000')
        if d < dmin and vec not in L:
            dmin = d
            mpp = vec
    return mpp

"""
O = find_center(L2)
v = dico['202-383-7824']
d = ed(v,O)
print(d)
"""
print(MPP(L4,dico))


                
        
        
    

        
