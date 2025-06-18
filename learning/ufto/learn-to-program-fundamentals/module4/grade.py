# 1
exp1 = len('deed') == 4
exp2 = "bit" in "habit"

print(exp1)
print(exp2)

# 2
exp3 = len("")

print(exp3)

# 3
dance_style = "Vogue"
exp4 = dance_style[2]
exp5 = dance_style[-3]

print(exp4)
print(exp5)

# 4 
title = "Queen"
exp6 = title[1]

print(exp6)

# 5
s = "pineapple"
exp7 = s[4:len(s)]
exp8 = s[-5:]

print(exp7)
print(exp8)

# 6 
prefix = "mad"
exp9 = prefix[:1] + prefix[1:3] + prefix[-2] + prefix[0]
print(exp9)

# 7
exp10 = 'apple'.upper().isupper()
exp11 = 'abc123'.isalnum()

print(exp10)
print(exp11)

# 8
s = "123"
exp12 = s.isalpha() or s.isnumeric()

print(exp12)

# 9
s1 = "I'm late! I'm late"
s2 = "late";

exp13 = s1.find(s2)
exp14 = s1.find(s2, 5)

print(exp13)
print(exp14)

s1 = "banana"
s2 = "ana" 

exp15 = s1.find(s2,s1.find(s2) + 1)

# 10
digits = '0123456789'
result = 0

for digit in digits:
    result = result + int(digit)

print(result) # 45

# 11
digits = '0123456789'
result = 0

for digit in digits:
    result = digit

print(result) # 9

# 12
digits = '0123456789'
result = ''

for digit in digits:
    result = result + digit * 2

print(result) # 00112233445566778899

# 13
message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

print(new_message)

message = 'Happy 29th!'
new_message = ''

for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)

print(new_message)

# 14
s1 = "abb"
s2 = "ab"
res = ''
for ch in s1:
    if ch in s2:
        res = res + ch
print(res)