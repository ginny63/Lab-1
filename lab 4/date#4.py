from datetime import datetime
def difsec(date2, date1):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds

dat1 = datetime.strptime('2022-12-18 00:00:00', '%Y-%m-%d %H:%M:%S')
dat2 = datetime.now()
print("\n%d seconds" % (difsec(dat2, dat1)))




