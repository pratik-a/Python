from datetime import datetime

def main():
    
    today = datetime.now()
    print(today.strftime("%a,%d %B %y"))
    
    print(today.strftime("date and time %C"))
    print(today.strftime("date %x"))
    print(today.strftime("time %X"))
    
    print(today.strftime("time : %I:%M:%S %p"))
    print(today.strftime("24 hr time : %H:%M"))
    

if __name__ =="__main__":
    main()
