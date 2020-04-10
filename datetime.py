import math
import os
import random
import re
import sys
import datetime

t1 ='Sun 10 May 2015 13:54:36 -0700'
t2 ='Sun 10 May 2015 13:54:36 -0000'

dt1 = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')# convert string to datetiem with timezon

dt2 = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')

timespand = dt2 -dt1  # calculate timespand

print(dt1)
print(dt2)
print(str(abs(timespand.days*24*3600 + timespand.seconds)) #return in second
