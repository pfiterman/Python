s = "123456"
digits = ""

for ch in s:
    if ch.isdigit():
        digits = digits + ch

print(f"digits = {digits}")
