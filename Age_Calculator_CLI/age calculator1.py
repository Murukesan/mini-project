#**** AGE CALCULATOR ****

import datetime
def year_checker():
    current=datetime.datetime.now()
    while True:
        birth_year=input("Which year you born:")
        if(birth_year.isdecimal()):
            if(int(birth_year)>=1000 and int(birth_year)<=current.year):
                return int(birth_year)
        print("It is not a valid year..please enter again.")

def month_checker():
    while True:
        birth_month=input("Which month you born:")
        if(birth_month.isdecimal()):
            if(int(birth_month)>=1 and int(birth_month)<=12):
                return int(birth_month)
        print("It is not a valid month...please enter again.")

def date_checker():
    while True:
        birth_date=input("Enter your birth date:")
        if(birth_date.isdecimal()):
            if(int(birth_date)>=1 and int(birth_date)<=31):
                return int(birth_date)
        print("It is not a valid date..please enter again.")

def process(year,month,date):
    current=datetime.datetime.now()
    dob=datetime.datetime(year,month,date)
    age=(current-dob)
    leap=[]
    while(year<current.year):
        if year%4==0 and year%100!=0:
            leap.append(year)
        if year%100==0 and year%400==0:
            leap.append(year)
        year+=1    
    years=(age.days-len(leap))//365
    months=age.days*0.032855
    days=age.days
    weeks=days//7
    hours=days*24
    minutes=hours*60
    seconds=minutes*60
    if(current.month==month and current.day==date):
        print(f"It is your {years}th Birthday....HAPPY BIRTHDAY!!!")
    print("========================================================")
    print("                     AGE CALCULATOR                     ")
    print("========================================================")
    print("Your AGE is                     :",years)
    print("LEAP YEARS Which Will you Lived :",*leap)
    print("Number of DAYS    Lived         :",days)
    print("Number of MONTHS  Lived         :",int(months))
    print("Number of WEEKS   Lived         :",weeks)
    print("Number of HOURS   Lived         :",hours)
    print("Number of MINUTES Lived         :",minutes)
    print("Number of SECONDS Lived         :",seconds)
    
    
if __name__=="__main__":
    while True:
        year=year_checker()
        month=month_checker()
        date=date_checker()
        process(year,month,date)
        choice=input("If you want calculate again type(y or Y)? OR press Enter to Exit...")
        if(choice=="Y" or choice=="y"):
            print("Re Enter The Details..")
            continue
        print("Thank You!!!")
        break

        
    
