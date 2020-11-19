import tkinter as tk


ans = 0
sum = 0
sumflag = 0
plusflag = 0
minusflag = 0
flag = 0
def one():
        label.set(1)
        global ans
        global flag
        flag = 0
        ans = 1
    
    
def two():
        label.set(2)
        global ans
        global flag
        flag = 0
        ans = 2
    

def plus():
    global sumflag
    global plusflag
    global minusflag
    global sum
    global ans
    global flag
    if flag == 0:
        flag = 1
        if sumflag == 0:
            if minusflag == 1:
                sum = sum - ans
                label.set(sum)
                minusflag = 0
            else:
                sum = sum + ans
                label.set(sum)
                sumflag = 1
                plusflag = 1
        else:
            sum = sum + ans
            label.set(sum)
    else:
        pass
    
    
def minus():
    global sumflag
    global plusflag
    global minusflag
    global ans
    global sum
    global flag
    if flag == 0:
        flag = 1
        if sumflag == 0:
            if plusflag == 1:
                sum = sum + ans
                label.set(sum)
                plusflag = 0
            else:
                sum = ans - sum
                label.set(sum)
                sumflag = 1
                minusflag = 1
        else:
            sum = sum - ans
            label.set(sum)
    else:
        pass
        
        

def answer():
    global sum
    global ans
    global plusflag
    global minusflag
    global flag
    flag = 1
    if plusflag == 1:
        sum = sum + ans
        plusflag = 0
    else:
        sum = sum - ans
        minusflag = 0
    label.set(sum)


def riset():
    label.set(0)
    global sum
    global sumflag
    global flag
    flag = 0
    sumflag = 0
    sum = 0


#最初の画面
base = tk.Tk()
base.geometry("700x700")
base.title("電卓")
label = tk.StringVar()
input_label = tk.Label(base,textvariable=label)
input_label.place(x=100, y=10)
button = tk.Button(base,text="１",width=10,height=5,command=one)
button.place(x=70, y=100)
button2 = tk.Button(base,text="２",width=10,height=5,command=two)
button2.place(x=70, y=200)
button3 = tk.Button(base,text="＋",width=10,height=5,command=plus)
button3.place(x=150, y=100)
button4 = tk.Button(base,text="－",width=10,height=5,command=minus)
button4.place(x=150, y=200)
button5 = tk.Button(base,text="＝",width=10,height=5,command=answer)
button5.place(x=100, y=300)
button6 = tk.Button(base,text="リセット",width=10,height=5,command=riset)
button6.place(x=100, y=400)
base.mainloop()