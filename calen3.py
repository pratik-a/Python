import calendar

c = calendar.TextCalendar(calendar.MONDAY);

#meeting will be on first friday of every month

for m in range(1,13):
    cal = calendar.monthcalendar(2022,m)
    wk1 = cal[0];
    wk2 = cal[1];
    
    if wk1[calendar.FRIDAY] != 0:
        meet = wk1[calendar.FRIDAY]
    else:
        meet = wk2[calendar.FRIDAY]

    print("%10s %2d"%(calendar.month_name[m],meet))