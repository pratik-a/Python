from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

def main():
    
    today = datetime.now()
    print(today)
    print("one year later", today+timedelta(365))
    print("2 day later", today+timedelta(days=2))
    print("2 day earlier", today-timedelta(days=2))

if __name__ =="__main__":
    main()
