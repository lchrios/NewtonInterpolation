from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import Proyecto as Algorithm
import Algorithm as alg

raiz = Tk()

arr = StringVar()
res = StringVar()
n = StringVar()
d = StringVar()
roots = StringVar()
form = StringVar()
filePath = StringVar()
destPath = StringVar()

raiz.title("Newton-Interpolation method")
raiz.resizable(False,False)
raiz.iconbitmap("tec.ico")
raiz.geometry("1024x512")
raiz.config(bd="10")
raiz.config(bg="#24252a")

frame = Frame(raiz, width="1024", height="768")
frame.config(bg="#24252a")
frame.pack()

title = Label(frame, text="Newton-Interpolation", fg="white", font=("Times New Roman",25),bg="#24252a")
title.grid(row=0,column=0, columnspan=2)

introLabel = Label(frame, fg="white", text="Introduce the point's values separated by a comma ,\nand to separate points just leave a blank space", font=("Times New Roman",14),bg="#24252a")
introLabel.grid(row=1,column=0, columnspan=2)
introHint = Label(frame, text="For a set of points S, where a(x,y), b(x,y), c(x,y) are points in the plane \nEx: a(1,1), b(2,4), c(3,9) = 1,1 2,4 3,9\nNote: #(S) > power of f(x)", font=("Times New Roman",14), fg="grey",bg="#24252a")
introHint.grid(row=2,column=0, columnspan=2)
inputLabelNum = Label(frame, fg="white", text="Introduce the distance:", font=("Times New Roman",14),bg="#24252a")
inputLabelNum.grid(row=3,column=0, columnspan=1, ipady="15")
inputLbBox = Label(frame, fg="white", text="Introduce the points as shown avove", font=("Times New Roman",14),bg="#24252a")
inputLbBox.grid(row=3,column=1,columnspan=1)
inputNum = Entry(frame, font="14", width="10", textvariable=d, bg="#81cfe0")
inputNum.grid(row=4,column=0,columnspan=1)
inputBox = Entry(frame, font="14", width="30", textvariable=arr, bg="#81cfe0")
inputBox.grid(row=4,column=1, columnspan=1)

inputLabel4 = Label(frame, fg="white", text="Results", font=("Times New Roman",18),bg="#24252a")
inputLabel4.grid(row=5,column=0, columnspan=1, ipady="30")

resLbD = Label(frame, fg="white", text="Calculated values:", font=("Times New Roman",18),bg="#24252a")
resLbD.grid(row=6,column=0,columnspan=1)
resBox = Entry(frame, font="18",width="20", state=DISABLED, textvariable=res)
resBox.grid(row=7,column=0,columnspan=1,rowspan=1,ipady="10")
formBox = Entry(frame, font="18", width="20", state=DISABLED, textvariable=form)
formBox.grid(row=8,column=0,columnspan=1,rowspan=1,ipady="10")

"""fileInLabel = ttk.LabelFrame(frame, text="Select the file's path:")
fileInLabel.grid(row=6,column=1,columnspan=1,rowspan=1)"""

fileInBox = Entry(frame, font="12", width="20", textvariable=filePath)
fileInBox.grid(row=6,column=1,columnspan=1,rowspan=1)
fileOutLabel = Label(frame, fg="white", text="Select the file's path:", font=("Times New Roman",12),bg="#24252a")
fileOutLabel.grid(row=7,column=1,columnspan=1,rowspan=1)
fileOutBox = Entry(frame, font="12", width="20", textvariable=destPath)
fileOutBox.grid(row=8,column=1,columnspan=1,rowspan=1)

def openFile():
    filename = filedialog.askopenfilename(initialdir = "/", title="Select a file to read...", filetype=(("Text doc","*.txt"),("All files","*.*")))
    filePath.set(filename)


def matplotCanvas(self,x,y):
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(x,y)

    canvas = FigureCanvasTkAgg(f, self)
    #canvas.show()
    canvas.get_tk_widget().grid(row="0",column="2",rowspan="9")

def polyToString(poly):
    print(poly)
    r = ""
    for i in range(len(poly)):
        if (poly[i] != 0):
            if (i == 0):
                r += str(poly[i])
            elif(i == 1):
                r += ("+" if poly[i] > 0 else "")+ str(poly[i]) + "x"
            elif(i >= 2):
                r += ("+" if poly[i] > 0 else "") +str(poly[i]) + "x^" + str(i)
    return r

def writeFile():
    dirPath = filedialog.askdirectory(initialdir="/", title="Select a destination to wrie...")
    destPath.set(dirPath)
    fp = open(filePath.get(),"r")
    r = []
    cnt = 1
    # Read and process every line
    for line in fp:
        a = line.split("|")
        eV = a[1].split(",")
        eX = float(eV[0])
        eY = float(eV[1])
        points = a[0].split()
        x = []
        y = []
        # Save all points for plotting
        for i in range(len(points)):
            zL = points[i].split(",")
            x.append(float(zL[0]))
            y.append(float(zL[1]))
        time, poly = Algorithm.NewtonInterpolation(x, y, eX)
        toWrite = "{}) f({})={} => f(x)={} | Resultado: {}".format(cnt,eX,time,polyToString(poly),time==eY)
        r.append(toWrite)

        cnt-=-1
    fp.close()
    fw = open(dirPath+"/result.txt","w+")
    for str2write in r:
        fw.write(str2write)
        fw.write("\n")

    fw.close()






def getIndexFor(v,arr):
    for i in range(len(arr)):
        if(arr[i] > v):
            print("index: {}".format(i))
            return i
    return i+1

def solve():
    if(d.get()==""):
        raise Exception("Introduzca una distancia.")
    a = arr.get().split()
    a = "-1,9 0,16 1,9 2,0 3,25".split()
    dis = float(str(d.get()))
    dis = -2.0
    x = []
    y = []
    # Save all points for plotting
    for i in range(len(a)):
        r = a[i].split(",")
        x.append(float(r[0]))
        y.append(float(r[1]))


    time, poly = Algorithm.NewtonInterpolation(x,y,dis)
    index = getIndexFor(dis,x)
    print(index)
    x.insert(index,dis)
    y.insert(index,time)

    res.set("t({}) = {}".format(dis,time))
    form.set("f(x)={}".format(polyToString(poly).lstrip("PY_VAR56")))
    matplotCanvas(frame,x,y)

btn = Button(frame)
btn.config(text="Open", command=openFile)
btn.grid(row=5, column=1, columnspan=1)

btn = Button(frame)
btn.config(text="Generate solutions", command=writeFile)
btn.grid(row=9, column=1, columnspan=1)


button = Button(frame)
button.config(text="Evaluate", command=solve)
button.grid(row=9, column=0, columnspan=1)













raiz.mainloop()
