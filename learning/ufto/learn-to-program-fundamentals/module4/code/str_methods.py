import math

exp1 = math.sqrt(4.0) # 2.0
exp2 = "I'm late! I'm late! For a very important date!"
exp3 = exp2.lower() # i'm late! i'm late! for a very important date!
print(exp2) # "I'm late! I'm late! For a very important date!"

exp4 = exp2.count("ate") # 3
exp5 = "computer".capitalize() # Computer
exp6 = "Computer".capitalize() # Computer
exp7 = exp2.find("late") # 4  first ocurrence
exp8 = exp2.find("late", 7) # 14   starts or after character 7
exp9 = exp2.find("moogah") # -1 str wasn't found
exp10 = exp2.rfind("late") # 14

exp11 = "     I'm feeling spaced out.     "
exp12 = exp11.lstrip() # "I'm feeling spaced out.     "
exp12 = exp11.rstrip() # "     I'm feeling spaced out."
exp12 = exp11.strip() # "I'm feeling spaced out."
