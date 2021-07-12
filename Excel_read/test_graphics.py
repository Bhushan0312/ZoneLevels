from tkinter import *
class graph():
    def __init__(self):

        self.root = Tk()
        root= self.root
        root.title("Test Graphics")
        root.geometry("350x500")
        root.configure(bg='white')
    def Text_Box(self,h,w,x,y):
        T = Text(self.root,height=h,width=w)
        T.place(x=x,y=y)
    def Button_click(self,text1,x,y,cmd):
        Search=Button(self.root,text=text1,font=("arial",10),command=cmd)
        Search.place(x=x,y=y)
        self.root.mainloop()
    def Label_text(self,text1):
        label1=Label(self.root,text=text1,font=("arial",10,"bold"))
        label1.place(x=10,y=40)
        self.root.mainloop()
        #label2 = Label(root,text="CMP : ",font=("arial",10))
        #label2.place(x=10,y=60)
        #label3 = Label(root,text="BUY : ",font=("arial",10))
        #label3.place(x=10,y=80)
        #label4 = Label(root,text="TARGET FOR BUY : ",font=("arial",10))
        #label4.place(x=10,y=100)
        #label5 = Label(root,text="SELL : ",font=("arial",10))
        #label5.place(x=10,y=120)
        #label6 = Label(root,text="SELL TARGET : ",font=("arial",10))
        #label6.place(x=10,y=140)
        #close = Button(root,text="Close",width=15,command=quit)
        #close.place(x=200,y=160)

