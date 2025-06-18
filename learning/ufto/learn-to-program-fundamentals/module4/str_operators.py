solution = "cat"
exp1 = solution == "cat" # True
exp2 = solution != "cat" # False

solution = "dog"
exp3 = solution == "cat" # False
exp4 = solution != "cat" # True

exp5 = "abracadabra" < "ace" # True
exp6 = "abracadabra" > "ace" # False

exp7 = "a" <= "a" # True
exp8 = "A" <= "B" # True
exp9 = "a" != "A" # True
exp10 = "a" < "A" # False
exp11 = "a" > "A" # True
exp12 = "," < "3" # True
exp13 = "s" == "3" # False

# exp14 = "s" <= 3  # TypeError str() <= int()

exp15 = "cad" in "abacadabra" # True
exp16 = "c" in "aeiou" # False
exp17 = "zoo" in "ooze" # False
exp18 = "" in "abc" # True
exp19 = "" in "" # True

exp20 = len("") # 0
exp21 = len("abacadabra") # 11
exp22 = len("Bwa" + "ha" * 10) # 23