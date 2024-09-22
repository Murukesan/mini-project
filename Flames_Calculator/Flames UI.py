#---------- FLAMES calculator ----------
from tkinter import *
from tkinter import messagebox
import re

def process():
    root=Tk()

    st1=StringVar()
    st2=StringVar()

    def clear():
        name1.delete(0,END)
        name2.delete(0,END)

        st1.set("")
        st2.set("")
        name1.focus_set()
    
    def procedure(common):
        flames=["Friends","Love","Affection","Marriage","Enemy","Siblings"]
        while(len(flames)>1):
            i=common
            while(len(flames)<i):
                i=i-len(flames)
            flames=flames[i:]+flames[:i-1]
        return flames[0]

    def compare(first_name,second_name):
        c=list(first_name.lower())
        d=list(second_name.lower())
        temp1=c[:]
        temp2=d[:]
        for i in temp1:
            if i in d:
                k=i
                c.remove(k)
                d.remove(k)
        common=len(c)+len(d)
        return common
    def checker(a,b):
        remove_char=["@","."," "]
        pattern=re.compile(r"[a-zA-Z\.\@]+")
        c="".join(i for i in a if not i in remove_char)
        d="".join(i for i in b if not i in remove_char)
        if re.fullmatch(pattern,c):
            if re.fullmatch(pattern,d):
                return c,d
        print("   Please enter a valid name")
        messagebox.showerror("ERROR","Not a valid name")
        return -1
    def calc_clear():
        st1.set("")
        st2.set("")
        name1.focus_set()
    
    def calculation():
        calc_clear()
        a=name1.get()
        b=name2.get()
        if a=="" or b=="":
            print("Please Type a input")
            messagebox.showerror("ERROR","type a input")
            calc_clear()
            return
        else:
            result=checker(a,b)
            if result == -1:
                clear()
                return
            else:
                first_name,second_name = result
                common=compare(first_name,second_name)
                if(common>=1):
                    st1.set(common)
                else:
                    print("We cannot find flames")
                    messagebox.showerror("ERROR","We can't find flames")
                result=procedure(common)
                st2.set(result)
    root.title("Flames Calculator")
    root.configure(bg="light blue")
    title=Label(root,text="FLAMES      ",font=("bold",20),bg="light blue")
    lab1=Label(root,text="First name        :",font=("bold",15),bg="light blue")
    lab2=Label(root,text="Second name   :",font=("bold",15),bg="light blue")
    lab3=Label(root,text="Unique count    :",font=("bold",15),bg="light blue")
    lab4=Label(root,text="Relationship       :",font=("bold",15),bg="light blue")

    title.grid(row=1,column=1)
    lab1.grid(row=8,column=0)
    lab2.grid(row=9,column=0)
    lab3.grid(row=11,column=0)
    lab4.grid(row=12,column=0)

    but1=Button(root,text="calculate",bg="yellow",font=("bold",10),command=calculation)
    but2=Button(root,text="Clear",bg="yellow",font=("bold",10),command=clear)

    but1.grid(row=10,column=1)
    but2.grid(row=13,column=1)

    name1=Entry(root)
    name2=Entry(root)

    unique=Entry(root,textvariable=st1,state="readonly")
    result=Entry(root,textvariable=st2,state="readonly")

    name1.grid(row=8,column=1)
    name2.grid(row=9,column=1)
    unique.grid(row=11,column=1)
    result.grid(row=12,column=1)

    root.mainloop()

if __name__=="__main__":
    process()
