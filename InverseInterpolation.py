#Functions

def NewtonInterpolation(x,y): 
    n = len(x)

    # ------------ Create Matrix ---------------#
    fdd = [[0 for i in range(n)] for j in range(n)]  
    for i in range(n):   
        fdd[i][0] = y[i]  
        
    # fdd[i rows][0 column] are y's
    # fdd[0 row][j columns] are b's
    
    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1]-fdd[i][j-1])/(x[i+j]-x[i])  
    #-------------------------------------------#

    # ------------ Calculate Polynomial -------------#
    polynomials = [1]*len(fdd[0]) 
    for i in range(len(fdd[0])):
        if polynomials[i] == 1:
            if i == 1: 
                polynomials[i] = [-x[i-1],1]
            elif i > 1:  
                polynomials[i] = polyMulti(polynomials[i-1],[-x[i-1],1])  
    
    # Multiply by their b
     
     
    for i in range(len(fdd[0])): 
        
        if isinstance(polynomials[i],list): 
            for j in range(len(polynomials[i])):
                polynomials[i][j] = polynomials[i][j]*fdd[0][i]
        else:
            polynomials[i] = polynomials[i] * fdd[0][i]
            
    #print(polynomials)

    #Sum Polynomials
    finalPoly = [0]*len(polynomials[len(polynomials)-1])

    for i in range(len(polynomials)): 
        if i == 0:
            finalPoly[i] = finalPoly[i] + polynomials[i]
        else:
            for j in range(len(polynomials[i])):
                finalPoly[j] = finalPoly[j] + polynomials[i][j] 
    return finalPoly
    # -----------------------------------------------#
     
def polyMulti(A,B):
    grad = (len(A)-1)+(len(B)-1) 
    res = [0]*(grad+1)
    for i in range(len(A)):
        for j in range(len(B)):
            res[i+j] = res[i+j] + (A[i] * B[j])
    return res
 
def derivatePoly(A): 
    if len(A) > 2:
        B = [0 for i in range(len(A)-1)] 
        for i in range(1,len(A)): 
            B[i-1] = (i+1)*A[i]
        return B
    else:
        return [A[1]]
 
def evalua(f,x): 
    a = f.copy()
    b = x
    evaluation = f[0] 
    if len(f)>1: 
        for i in range(1,len(a)): 
            a[i] = a[i]*(b**i) 
            evaluation = evaluation + a[i]
    return evaluation

def NewRap(x,f,maxiter,error):
    xold = x
    fprime = derivatePoly(f)  
    itera = 0
    ea = 100 
    while itera < maxiter and ea > error: 
        fold = evalua(f,xold) 
        fpold = evalua(fprime,xold)  
        dif = fold / fpold 
        xnew = xold - dif   
        if xnew != 0:
            ea = abs((xnew-xold)/xnew)*100  
        xold = xnew
        itera = itera + 1
    return xold

 
 


#Input 

"""n = int(input("How many points do you have?\n"))

#Create Table
points = [[0 for i in range(n)]for i in range(2)] 
for i in range(2):
    for j in range(n):
        if i==0:
            nval = float(input("Introduce your "+str(j+1)+" value in x:\n"))
        else:
            nval = float(input("Introduce your "+str(j+1)+" value in y:\n"))
        points[i][j] = nval 

xeval = float(input("Introduce your new value in f(x)?\n"))

funct = NewtonInterpolation(points[0],points[1])
funct[0] = funct[0]-xeval  
root = NewRap(100, funct, 100, .00000000000000000000000001) 

print("The x value for the given f(x) is {}".format(root))"""


