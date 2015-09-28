#39.     Clock Angle
#We are given a specific time(like 02:23), 
#weneed to get the angle between hour 
#and minute(less than 180)





s='02:23'
def clockangle(s):
    unit_min_angle=360/60
    unit_hour_angle=360/12
    hour=int(s[0:2])
    mi=int(s[3:])

    mi_angle=mi*unit_min_angle

    hour_angle=hour*unit_hour_angle

    diff=abs(mi_angle-hour_angle)

    return diff if diff<=180 else 360-diff

print clockangle(s)
