import time
import calendar
localtime = time.localtime(time.time())
localtime_day = localtime.tm_mday
localtime_format = time.asctime(localtime)


print(localtime_format)

count = 0
cal = calendar.month(2021,12)
print(cal)
for thang in range(1,13):
    for week in calendar.monthcalendar(2022, thang):
        for mday in week:
            if(mday != 0):
                count += 1
    print("Tháng " + str(thang) + " : " + str(count) + " ngày")
    count = 0