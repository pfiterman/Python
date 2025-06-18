# 0   1   2   3   4   5   6   7  8  9  10  11 12  13 14 15
# L   e   a   r   n       t   o     P  r   o   g  r  a  m
#-16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6  -5  -4 -3 -2 -1

s = "Learn to Program"
s[0] = "L"
s[1] = "e"
s[2] = "a"
s[-1] = "m"
s[-2] = "a"
s[-3] = "r"

slice1 = s[0:5] # Learn
slice2 = s[6:8] # to
slice3 = s[9:16] # Program
slice4 = s[9:len(s)] # Program
slice5 = s[9:] # Program
slice6 = s[:8] # Learn to
slice7 = s[:] # Learn to Program

slice8 = s[1:8] # earn to
slice9 = s[1:-8] # earn to
slice10 = s[-15:-8] # earn to

s[6] = "d" # TypeError 'str' does not support item assignment
s[9:16] = "run" # TypeError 'str' does not support item assignment

slice11 = s[:5] + "ed" + s[5:] # Learned to Program
