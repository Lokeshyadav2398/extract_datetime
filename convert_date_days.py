import datetime
past_date = "2016-12-29T10:30:07"
future_date = "2017-11-29T11:29:11"
(date,time) = past_date.split("T")
year, month, day = date.split("-")
	
(hour,minu,sec) = time.split(":")
	
past = datetime.datetime(int(year),int(month),int(day),int(hour),int(minu),int(sec))
print(past)

(fd,ft) = future_date.split("T")
yy, mm, dd = fd.split("-")
	
hh,min,ss = ft.split(":")
	
present = datetime.datetime(int(yy),int(mm),int(dd),int(hh),int(min),int(ss))
print(present)
	
print((present-past).days,"days")
