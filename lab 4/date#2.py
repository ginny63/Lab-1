from datetime import date,timedelta
td=date.today()
print("Today is: ",td)
ys=td-timedelta(days=1)
print("Yesterday was: ",ys)
tm=td+timedelta(days=1)
print("Tomorrow is: ",tm)