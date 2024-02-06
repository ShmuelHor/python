import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%c"))
print(x)

y = datetime.datetime(2020,5,7)
print(y)
print(y.strftime("%B"))
