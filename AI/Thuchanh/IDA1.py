import queue
import numpy as np
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt
from matplotlib import colors
import copy
import numpy.random as rd
import time
import profile

class Cube():
    def __init__(self):
        self.F=[[0,0],[0,0]] 
        self.B=[[1,1],[1,1]] 
        self.U=[[2,2],[2,2]] 
        self.D=[[3,3],[3,3]] 
        self.L=[[4,4],[4,4]] 
        self.R=[[5,5],[5,5]] 
        self.N=[[6,6],[6,6]]
        self.liste = [self.F,self.B,self.U,self.D,self.L,self.R]
        [F,B,U,D,L,R]=self.liste
 
    def liste(self):
        return([self.F,self.B,self.U,self.D,self.L,self.R])
 
    def up(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        U[0][0],U[0][1],U[1][1],U[1][0]=U[1][0],U[0][0],U[0][1],U[1][1]
        B[0][1],B[0][0],R[0][1],R[0][0],F[0][1],F[0][0],L[0][1],L[0][0]=L[0][1],L[0][0],B[0][1],B[0][0],R[0][1],R[0][0],F[0][1],F[0][0]
 
    def uprev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        U[0][0],U[0][1],U[1][1],U[1][0]=U[0][1],U[1][1],U[1][0],U[0][0]
        B[0][1],B[0][0],R[0][1],R[0][0],F[0][1],F[0][0],L[0][1],L[0][0]=R[0][1],R[0][0],F[0][1],F[0][0],L[0][1],L[0][0],B[0][1],B[0][0]
 
    def right(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        R[0][0],R[0][1],R[1][1],R[1][0]=R[1][0],R[0][0],R[0][1],R[1][1]
        U[1][1],U[0][1],B[0][0],B[1][0],D[1][1],D[0][1],F[1][1],F[0][1]=F[1][1],F[0][1],U[1][1],U[0][1],B[0][0],B[1][0],D[1][1],D[0][1]
 
    def rightrev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        R[0][0],R[0][1],R[1][1],R[1][0]=R[0][1],R[1][1],R[1][0],R[0][0]
        U[1][1],U[0][1],B[0][0],B[1][0],D[1][1],D[0][1],F[1][1],F[0][1]=B[0][0],B[1][0],D[1][1],D[0][1],F[1][1],F[0][1],U[1][1],U[0][1]
 
    def back(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        B[0][0],B[0][1],B[1][1],B[1][0]=B[1][0],B[0][0],B[0][1],B[1][1]
        U[0][0],U[0][1],R[0][1],R[1][1],D[1][1],D[1][0],L[1][0],L[0][0]=R[0][1],R[1][1],D[1][1],D[1][0],L[1][0],L[0][0],U[0][0],U[0][1]
    def backrev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        B[1][0],B[0][0],B[0][1],B[1][1]= B[0][0],B[0][1],B[1][1],B[1][0]
        R[0][1],R[1][1],D[1][1],D[1][0],L[1][0],L[0][0],U[0][0],U[0][1]=U[0][0],U[0][1],R[0][1],R[1][1],D[1][1],D[1][0],L[1][0],L[0][0]
 
    def front(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        F[1][0],F[0][0],F[0][1],F[1][1]= F[1][1],F[1][0],F[0][0],F[0][1]
        U[1][0],U[1][1],R[0][0],R[1][0],D[0][1],D[0][0],L[1][1],L[0][1]=L[1][1],L[0][1],U[1][0],U[1][1],R[0][0],R[1][0],D[0][1],D[0][0]
 
    def frontrev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]        
        F[1][0],F[0][0],F[0][1],F[1][1]= F[0][0],F[0][1],F[1][1],F[1][0]
        U[1][0],U[1][1],R[0][0],R[1][0],D[0][1],D[0][0],L[1][1],L[0][1]=R[0][0],R[1][0],D[0][1],D[0][0],L[1][1],L[0][1],U[1][0],U[1][1]
 
    def left(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        L[1][0],L[0][0],L[0][1],L[1][1]= L[0][0],L[0][1],L[1][1],L[1][0]
        U[0][0],U[1][0],F[0][0],F[1][0],D[0][0],D[1][0],B[0][1],B[1][1]=B[0][1],B[1][1],U[0][0],U[1][0],F[0][0],F[1][0],D[0][0],D[1][0]
 
    def leftrev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        L[1][0],L[0][0],L[0][1],L[1][1]= L[1][1],L[1][0],L[0][0],L[0][1]
        U[0][0],U[1][0],F[0][0],F[1][0],D[0][0],D[1][0],B[0][1],B[1][1]=F[0][0],F[1][0],D[0][0],D[1][0],B[0][1],B[1][1],U[0][0],U[1][0]
 
    def down(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        D[1][0],D[0][0],D[0][1],D[1][1]= D[1][1],D[1][0],D[0][0],D[0][1]
        F[1][0],F[1][1],R[1][0],R[1][1],B[1][0],B[1][1],L[1][0],L[1][1]=L[1][0],L[1][1],F[1][0],F[1][1],R[1][0],R[1][1],B[1][0],B[1][1]
 
    def downrev(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        D[1][0],D[0][0],D[0][1],D[1][1]= D[0][0],D[0][1],D[1][1],D[1][0]
        F[1][0],F[1][1],R[1][0],R[1][1],B[1][0],B[1][1],L[1][0],L[1][1]=R[1][0],R[1][1],B[1][0],B[1][1],L[1][0],L[1][1],F[1][0],F[1][1]
 
    def applique(self,s):
        def listmove(L,M): 
            if L == "":
                return M
            elif L[-1]=="'":
                M.append(L[-2:])
                return listmove(L[:-2],M)
            else:
                M.append(L[-1])
                return listmove(L[:-1],M)
        def ap(L):
            M=[]
            k=len(listmove(L,M))+1
            return [listmove(L,M)[-i] for i in range(1,k)]  
 
        L=ap(s)
        for i in L:
            if i=="U" :
                self.up()
            elif i=="U'" :
                self.uprev()
            elif i=="R":
                self.right()
            elif i=="R'":
                self.rightrev()
            elif i=="B":
                self.back()
            elif i=="B'":
                self.backrev()
            elif i=="F":
                self.front()
            elif i=="F'":
                self.frontrev()
            elif i=="D":
                self.down()
            elif i=="D'":
                self.downrev()
            elif i=="L":
                self.left()
            elif i=="L'":
                self.leftrev()   
 
    def resolu(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
        L = [F, B, U, D, L, R]
        for i in L:
                print(i)
                if i[0][0]!=i[0][1] or i[0][0]!=i[1][0] or i[0][0]!=i[1][1]:
                    return(False)
        return(True)
 
    def dessin(self):
        [F,B,U,D,L,R]=[self.F,self.B,self.U,self.D,self.L,self.R]
 
        M = np.array([[6, 6, U[0][0], U[0][1], 6, 6, 6, 6],
 
                       [6, 6, U[1][0], U[1][1], 6, 6, 6, 6],
 
                       [L[0][0], L[0][1], F[0][0], F[0][1], R[0][0], R[0][1], B[0][0], B[0][1]],
 
                       [L[1][0], L[1][1], F[1][0], F[1][1], R[1][0], R[1][1], B[1][0], B[1][1]],
 
                       [6, 6, D[0][0], D[0][1], 6, 6, 6, 6],
 
                       [6, 6, D[1][0], D[1][1], 6, 6, 6, 6]])
 
        cdict = colors.ListedColormap(['green','blue','white','yellow','orange','red','black'])
        plt.imshow(M, interpolation='nearest',cmap = cdict)
        plt.show()
 
def copie(C):
    K=Cube()
    L=""
    K.L=[list(x) for x in C[0].L]
    K.R=[list(x) for x in C[0].R]
    K.U=[list(x) for x in C[0].U]
    K.D=[list(x) for x in C[0].D]
    K.F=[list(x) for x in C[0].F]
    K.B=[list(x) for x in C[0].B]
    L=C[1]+""
    return [K,L]
def longueur(S): 
    L=list(S)
    K=0
    for i in L:
        if i!= "'":
            K+=1
    return K
 
 
def pasinvderniermove(S):
    Moves = {"U","U'","R","R'","B","B'"}
    forbidden =""
    if S!="" and S[-1] == "'" :
        forbidden= S[-2]
    elif S!="" and S[-1]!="'":
        forbidden= S[-1]+"'"
    return Moves - {forbidden}
def appliquemovesensemble(S,L):
    L1=[copie(L) for _ in range(longueur(S))]
    compteur = 0
    for i in S:
        L1[compteur][0].applique(i)
        L1[compteur][1]+=i
        compteur+=1
    return L1
def getchild(node):
    return appliquemovesensemble(pasinvderniermove(node[1]),node)
 
 
def dbs(C,k):
    L=queue.LifoQueue()
    L.put([C,""])
    while not L.empty() : 
        top = L.get()
        long=longueur(top[1])
        if long == k and top[0].resolu() : 
            return top
        if long<k:
            LCubes=getchild(top)
            for i in LCubes:
                L.put(i)
    return False
 
def mrd(C,N):
    L = ['U','R','B',"U'","R'","B'"]
    m = ''
    for i in range(N):
        k = rd.randint(0,6)
        m+=L[k]
    C.applique(m)
    return m
 
 
def iddfs(C):
    max=14
    for i in range(max+1):
        resultat=dbs(C,i)
        if resultat!= False:
            return resultat[1]
        break
    