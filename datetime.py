from datetime import datetime
from datetime import date
from datetime import time


def main():
    today = date.today()
    print("today date is ", today)
    print("today date is ", today.day, today.month, today.year)
    print("week day is ",today.weekday()) 

    today = datetime.now()
    print("today date and time is ", today)
    

if __name__ =="__main__":
    main()
