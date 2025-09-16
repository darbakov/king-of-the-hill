import datetime
now = datetime.datetime.today()
NY = datetime.datetime(now.year+1, 1, 1)
d = NY-now  
                    
mm, ss = divmod(d.seconds, 60)
hh, mm = divmod(mm, 60)

print('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
