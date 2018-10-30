#DayDayUpQ.py
dayUp = pow(1.001, 365)
dayDown = pow(0.999, 365)
print("向上: {:.2f}, 向下: {:.2f}".format(dayUp, dayDown))

dayFactor = 0.01
dayUp2 = pow(1+dayFactor, 365)
dayDown2 = pow(1-dayFactor, 365)
print("向上: {:.2f}, 向下: {:.2f}".format(dayUp2, dayDown2))

base = 1.0
dayFactor2 = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        base = base * (1 - dayFactor2)
    else:
        base = base * (1 + dayFactor2)
print("工作日的力量: {:.2f}".format(base))

def dayUp(df):
    base = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            base = base * (1 - 0.01)
        else:
            base = base * (1 + df)
    return base
dayFactor3 = 0.01
while dayUp(dayFactor3) < 37.78:
    dayFactor3 += 0.001
print("努力参数: {:.3f}".format(dayFactor3))
