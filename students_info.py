import tkinter as k
import mysql.connector as sq
import tkinter.messagebox 

cn=sq.connect(database='db1',user='root',password='root')
w=k.Tk()
w.title('stu')
w.geometry('200x200')

def m():
    w1=k.Tk()
    w1.title('mrks')
    w1.geometry('300x200')
    w1['bg']='pink'
    
    l1=k.Label(w1,text='rl',bg='yellow',font=('Arial',14))
    l2=k.Label(w1,text='nm',bg='yellow',font=('Arial',14))
    l3=k.Label(w1,text='s1',bg='yellow',font=('Arial',14))
    l4=k.Label(w1,text='s2',bg='yellow',font=('Arial',14))
    
    e1=k.Entry(w1,width=10)
    e2=k.Entry(w1,width=10)
    e3=k.Entry(w1,width=10)
    e4=k.Entry(w1,width=10)

    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    l4.grid(row=4,column=1)
    
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    e4.grid(row=4,column=2)
    def s():
        r=e1.get()
        nm=e2.get()
        s1=e3.get()
        s2=e4.get()
        c=cn.cursor()
        c.execute("insert into stu values(%s,%s,%s,%s)",params=(r,nm,s1,s2))
        cn.commit()
        tkinter.messagebox.showinfo(title='info',message='created')
        e1.delete(0,k.END)
        e2.delete(0,k.END)
        e3.delete(0,k.END)
        e4.delete(0,k.END)
        
    b1=k.Button(w1,text='save',command=s).grid(row=5,column=1)
            
b1=k.Button(w,text='marks',font=('Arial',14),command=m)
b1.pack(fill=k.BOTH,expand=True)

def f():
    w1=k.Tk()
    w1.title('mrks')
    w1.geometry('300x200')
    w1['bg']='blue'
    l1=k.Label(w1,text='rolno.',bg='yellow',font=('Arial',15))
    e1=k.Entry(w1,width=10)
    l1.grid(row=1,column=1)
    e1.grid(row=1,column=2)
    def n():
        r=e1.get()
        c=cn.cursor()
        c.execute("select r,nm,s1,s2,s1+s2 from stu where r=%s",params=(r,))
        rw=c.fetchone()
        if rw==None:
               tkinter.messagebox.showinfo(title='info',message='inv')
        else:
            rs='pass' if rw[2]>=40 and rw[3]>=40 else 'fail'
            a=map(str,rw)
            s=" ".join(a)
            s=s+" "+rs
            l2=k.Label(w1,text=s,font=('Arial',15)).grid(row=2,column=1)
            
    b1=k.Button(w1,text='find',command=n).grid(row=3,column=1)
    
b1=k.Button(w,text='fnd',font=('Arial',15),command=f)
b1.pack(fill=k.BOTH,expand=True)



