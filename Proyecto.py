def NewtonInterpolation(x,y,xeval):
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
    #print(finalPoly)
    # -----------------------------------------------#
     
    # ------ Estimate Value on Xeval ------ #
    xterm = 1
    yint = [0]*n
    yinter = 0
    yint[0] = fdd[0][0]
    for order in range(1,n):
        xterm = xterm * (xeval - x[order-1])
        yinter = yint[order-1] + fdd[0][order] * xterm
        yint[order] = yinter 

    return yint[order], finalPoly
    # ------------------------------------- #

def polyMulti(A,B):
    grad = (len(A)-1)+(len(B)-1) 
    res = [0]*(grad+1)
    for i in range(len(A)):
        for j in range(len(B)):
            res[i+j] = res[i+j] + (A[i] * B[j])
    return res
    


"""print("Bienvenido a la calculadora de velocidades")
n = int(input("Introduzca cuantos puntos de medicion experimental se tienen: "))
x = []
y = []
for i in range(n):
    x.append(int(input("Introduzca la posicion en el punto {}: ".format(i+1))))
    y.append(int(input("Introduzca el tiempo que tomó desde el inicio en el punto {}: ".format(i+1))))
evaluacion = int(input("Introduzca la distancia que se quiere recorrer para estimar el tiempo que le tomaría: "))



print("t({}) = {}".format(evaluacion,NewtonInterpolation(x,y,evaluacion)))"""
 






