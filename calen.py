import calendar

c = calendar.TextCalendar(calendar.MONDAY);
st = c.formatmonth(2022,01,0,0);
print(st);

hc = calendar.HTMLCalendar(calendar.MONDAY);
st = hc.formatmonth(2022,01);
print(st);

