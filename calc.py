import tkinter as tk


ans = 0 #数字のボタンを押した時格納する変数
sum = 0 #足し引きした際の合計の値を格納する変数
ansflag = 0 #一番初めに数字のボタンを押した際、sumに格納するためのフラグ
sumflag = 0 #足し引きボタンを押した際、計算結果を出すかどうか判定するフラグ
calcflag = 0 #連続で足し引きボタンを押した際、何も処理をしない為のフラグ
flag = 0 #足す計算か、引く計算をするか判定するフラグ

#１を押した際の処理
def one():
        label.set(1)
        global ans
        global sum
        global sumflag
        global ansflag
        global calcflag
        calcflag = 0
        ans = 1
        #一番初めに数字のボタンを押した時は、合計に格納させる
        if ansflag == 0:
            sum += ans
        ansflag = 1
    
#２を押した際の処理
def two():
        label.set(2)
        global ans
        global sum
        global sumflag
        global ansflag
        global calcflag
        calcflag = 0
        ans = 2
        #一番初めに数字のボタンを押した時は、合計に格納させる
        if ansflag == 0:
            sum += ans
        ansflag = 1
    

#　+ボタンを押した際の処理
def plus():
    global sumflag
    global calcflag
    global flag
    global ans
    global sum
    #連続で押した場合は何も処理しない
    if calcflag == 0:
        # =ボタンと同じ処理をさせる
        if sumflag == 1:
            if flag == 1:
                sum += ans
            elif flag == 2:
                sum -= ans
            label.set(sum)
            sumflag = 0
    calcflag = 1
    #足す処理をさせるフラグをセットする
    flag = 1
    sumflag = 1
    

    
    
def minus():
    global sumflag
    global calcflag
    global flag
    global ans
    global sum
    #連続で押した場合は何も処理しない
    if calcflag == 0:
        # =ボタンと同じ処理をさせる
        if sumflag == 1:
            if flag == 1:
                sum += ans
            elif flag == 2:
                sum -= ans
            label.set(sum)
            sumflag = 0
    calcflag = 1
    #引く処理をさせるフラグをセットする
    flag = 2
    sumflag = 1

        
        
# =ボタンを押した際の処理
def answer():
    global sum
    global ans
    global flag
    global sumflag
    #足すか引くかはflagで判定する
    if flag == 1:
        sum += ans
    elif flag == 2:
        sum -= ans
    label.set(sum)
    sumflag = 0


#リセットボタンを押した際の処理　合計の変数やフラグを処理化させる
def riset():
    label.set(0)
    global sum
    global sumflag
    global ansflag
    global flag
    flag = 0
    ansflag = 0
    sumflag = 0
    sum = 0


#最初の画面
base = tk.Tk()
base.geometry("700x700")
base.title("電卓")
label = tk.StringVar()
label2 = tk.StringVar()
input_label = tk.Label(base,textvariable=label)
input_label.place(x=100, y=10)
input_label2 = tk.Label(base,textvariable=label2)
input_label2.place(x=300, y=10)
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