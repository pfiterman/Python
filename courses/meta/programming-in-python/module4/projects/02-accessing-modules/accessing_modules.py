import sys

locations = sys.path
print(locations)

for l in locations:
    print(l)

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)