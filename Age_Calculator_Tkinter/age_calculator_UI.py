from tkinter import *
from tkinter import messagebox
import datetime

root = Tk()

st1=StringVar()
st2=StringVar()
st3=StringVar()
st4=StringVar()
st5=StringVar()
st6=StringVar()
st7=StringVar()

#The clear function delete all entry value in the root window.
def clear():
    birth_date.delete(0,END)
    birth_month.delete(0, END)
    birth_year.delete(0, END)

    st1.set("")
    st2.set("")
    st3.set("")
    st4.set("")
    st5.set("")
    st6.set("")
    st7.set("")
    birth_date.focus_set()
    
#The calc_clear function user do delete the invalid input.
def calc_clear():
    birth_date.delete(0,END)
    birth_month.delete(0, END)
    birth_year.delete(0, END)
    birth_date.focus_set()

def output_clear():
    st1.set("")
    st2.set("")
    st3.set("")
    st4.set("")
    st5.set("")
    st6.set("")
    st7.set("")
    birth_date.focus_set()
    
def check_error():
    if birth_date.get()=="" or birth_month.get()=="" or birth_year.get()=="":
        print("Please Type A input")
        messagebox.showerror("ERROR","Please Type a Input")
        calc_clear()
        return -1
    
def str_func(input_date,input_month,input_year):
    current=datetime.datetime.now()
    if(input_date.isdecimal() and input_month.isdecimal() and input_year.isdecimal()):
        if(int(input_date)>=1 and int(input_date)<=31 and int(input_month)>=1 and int(input_month)<=12 and int(input_year)>=1000 and int(input_year)<=current.year):
            return int(input_date),int(input_month),int(input_year)
    print("Check the Input..Type again")
    messagebox.showerror("ERROR","Invalid input")
    calc_clear()
    return -2


#The calculation function Gets the input from the the user and calculate the our age and other output values
def calculation():
    output_clear()
    result=check_error()
    if result==-1:
        return
    else:
        input_date=birth_date.get() 
        input_month=birth_month.get()
        input_year=birth_year.get()
        result1=str_func(input_date,input_month,input_year)
        if result1==-2:
            return
        else:
            date,month,year=result1
            current=datetime.datetime.now()
            leap = []
            leap_year=year
            while (leap_year < current.year):
                 if leap_year % 4 == 0 and leap_year % 100 != 0:
                    leap.append(leap_year)
                 if year % 100 == 0 and year % 400 == 0:
                    leap.append(leap_year)
                 leap_year += 1


            dob=datetime.datetime(year,month,date)
            age=current-dob
            total_days=age.days
            no_of_years=(total_days-len(leap))//365
            no_of_months=int(total_days*0.032855)
            no_of_weeks=total_days//7
            no_of_days=total_days
            no_of_hours=total_days*24
            no_of_minutes=no_of_hours*60
            no_of_seconds=no_of_minutes*60

            st1.set(no_of_years)
            st2.set(no_of_months)
            st3.set(no_of_weeks)
            st4.set(no_of_days)
            st5.set(no_of_hours)
            st6.set(no_of_minutes)
            st7.set(no_of_seconds)

if __name__=="__main__":
    root.title("AGE CALCULATOR")
    root.configure(bg="light blue")
    #We have create the labels.These three labels are user input labels.
    birth_date_label=Label(root,text=" Birth date   :",font=("bold",15),bg="light blue")
    birth_month_label=Label(root,text=" Birth month :",font=("bold",15),bg="light blue")
    birth_year_label=Label(root,text=" Birth year   :",font=("bold",15),bg="light blue")

    #These are the Output labels.
    years_label=Label(root,text="No of years lived     :",font=("bold",15),bg="light blue")
    months_label=Label(root,text="No of months lived   :",font=("bold",15),bg="light blue")
    weeks_label=Label(root,text="No of Weeks lived    :",font=("bold",15),bg="light blue")
    days_label=Label(root,text="No of days lived      :",font=("bold",15),bg="light blue")
    hours_label = Label(root, text="No of hours lived     :", font=("bold", 15),bg="light blue")
    minutes_label=Label(root,text="No of minutes lived  :",font=("bold",15),bg="light blue")
    seconds_label=Label(root,text="No of seconds lived :",font=("bold",15),bg="light blue")

    #Using grid we have do arrange the labels in order.
    birth_date_label.grid(row=1, column=0, padx=10, pady=10)
    birth_month_label.grid(row=2, column=0, padx=10, pady=10)
    birth_year_label.grid(row=3, column=0, padx=10, pady=10)

    years_label.grid(row=5, column=0, padx=10, pady=10)
    months_label.grid(row=6, column=0, padx=10, pady=10)
    weeks_label.grid(row=7, column=0, padx=10, pady=10)
    days_label.grid(row=8, column=0, padx=10, pady=10)
    hours_label.grid(row=9, column=0, padx=10, pady=10)
    minutes_label.grid(row=10, column=0, padx=10, pady=10)
    seconds_label.grid(row=11,column=0,padx=10,pady=10)

    #Buttons are Created.
    #calc_button process the input values and produce the output values in the corresponding Entries.
    calc_button = Button(root, text="Calculate", width=10, font=("bold", 10), bg="yellow", command=calculation)
    calc_button.grid(row=4, column=1, pady=10)

     

    #Clear Button clears all the entries.
    clear_button=Button(root,text="Clear",width=10,font=("bold",10),bg="yellow",command=clear)
    clear_button.grid(row=12,column=1,pady=10)

    #we have do create the entries.Entry is uesd to Get the input from the user.
    birth_date=Entry(root)
    birth_month = Entry(root)
    birth_year= Entry(root)

    years=Entry(root)
    years.configure(textvariable=st1,state="readonly")
    years.grid(row=5, column=1, padx=10, pady=10)
    months = Entry(root)
    months.configure(textvariable=st2,state="readonly")
    weeks=Entry(root)
    weeks.configure(textvariable=st3,state="readonly")
    days=Entry(root)
    days.configure(textvariable=st4,state="readonly")
    hours=Entry(root)
    hours.configure(textvariable=st5,state="readonly")
    minutes = Entry(root)
    minutes.configure(textvariable=st6,state="readonly")
    seconds = Entry(root)
    seconds.configure(textvariable=st7,state="readonly")
    
     
    #Using Grid we gave to arrange the Entries in order.
    birth_date.grid(row=1,column=1,padx=10,pady=15)
    birth_month.grid(row=2, column=1, padx=10, pady=15)
    birth_year.grid(row=3, column=1, padx=10, pady=10)

    
    months.grid(row=6, column=1, padx=10, pady=10)
    weeks.grid(row=7, column=1, padx=10, pady=10)
    days.grid(row=8, column=1, padx=10, pady=10)
    hours.grid(row=9, column=1, padx=10, pady=10)
    minutes.grid(row=10, column=1, padx=10, pady=10)
    seconds.grid(row=11, column=1, padx=10, pady=10)
    root.mainloop()
