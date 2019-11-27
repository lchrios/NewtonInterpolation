import math

class BairstrowAlgorithm():
    def Bairstrow(self,a,nn,es,rr,ss,maxit):
        re = [0] * (nn+2)
        im = [0] * (nn+2)
        r1 = 0
        r2 = 0
        i1 = 0
        i2 = 0
        #Crear arreglos de N tamaño
        b = [0]*nn
        c = [0]*nn
        d = [0]*nn
        #Establecer r, s y n
        r = rr
        s = ss
        n = nn
        #Establecer iteracion y errores
        iter = 0
        ea1 = 1
        ea2 = 1

        while n>3 and iter < maxit:
            iter = iter + 1
            b[n-1] = a[n-1]
            b[n-2] = a[n-2] + r*b[n-1]
            c[n-1] = b[n-1]
            c[n-2] = b[n-2] + r*c[n-1]
            for i in range(n-2,0,-1):
                b[i-1] = a[i-1] + r * b[i] + s * b[i+1]
                c[i-1] = b[i-1] + r * c[i] + s * c[i + 1]
            det = c[2]*c[2]-c[3]*c[1]
            if det != 0:
                dr = (-b[1]*c[2]+b[0]*c[3])/det
                ds = (-b[0] * c[2] + b[1] * c[1]) / det

                r = r + dr
                s = s + ds

                if(r != 0):
                    ea1 = abs(dr/r)*100
                if(s != 0):
                    ea2 = abs(ds/s)*100
            else:
                r = r + 1
                s = s + 1
                iter = 0
            self.Quadroot(r,s,r1,i1,r2,i2,re,im)
            k = n - 2
            for i in range(k):
                d[i] = round(b[i+2],2)
            if ea1 <= es and ea2 <= es or iter >= maxit:
                break


        if iter < maxit:
            if n == 2:
                r = -a[1] / a[2]
                s = -a[0] / a[2]
                self.Quadroot(r,s,r1,i1,r2,i2,re,im)
        else:
            iter = 1
        for i in range(len(d)-1,0,-1):
            if(d[i] == 0):
                d.pop(i)
        for i in range(len(im)):
            if(im[i]!=0 and im[i]>0):
                re[i] = str(re[i])+"+"+str(im[i])+"i"
            elif(im[i]!=0 and im[i]<0):
                re[i] = str(re[i]) + str(im[i]) + "i"
        if(len(d)==2):
            r3 = -d[0]/d[1]
            re[0] = round(r3,1)
        for i in range(len(re)-1,-1,-1):
            if(re[i]==0):
                re.pop(i)

        if (len(d) > 3):
            arr = self.Bairstrow(d, len(d), es, r, s, maxit)
            for i in range(len(arr)):
                re.append(arr[i])
        return re

    def Quadroot(self,r,s,r1,i1,r2,i2,re,im):
        disc = (r**2) +(4*s)
        if disc > 0:
            r1 = round((r + math.sqrt(disc))/2,6)
            r2 = round((r - math.sqrt(disc))/2,6)
            i1 = 0
            i2 = 0
        else:
            r1 = round(r/2,6)
            r2 = round(r1,6)
            i1 = round(math.sqrt(abs(disc))/2,5)
            i2 = -i1
        re[len(re)-1] = round(r1, 3)
        im[len(im)-1] = round(i1, 3)
        re[len(re)-2] = round(r2, 3)
        im[len(im)-2] = round(i2, 3)

"""a0 = [-22,32,-11,1], es = 1, r = s = .1, maxiter = 9
a1=[1.25,-3.875,2.125,2.75,-3.5,1], es = 1, r = s = -1, maxiter = 9
a2=[-4.069,6.2,-3.7,1], es = 1, r = s = .1, maxiter = 9
n = 4
es = 1
print(Bairstrow(a2,len(a2),es,.1,.1,9))

a1 = [-1.0, 0.5, 2.0, '1.0-0.5i', '1.0+0.5i']
a0 = [3.3, 1.0, 6.732], es = 1, r = s = .1
a2=[-4.069,6.2,-3.7,1],"""
