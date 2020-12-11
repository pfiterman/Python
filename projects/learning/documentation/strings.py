string = 'spam eggs'            # strings can be enclosed in single quotes
string1 = 'doesn\'t'            # use \' to escape the single quote...
string2 = "doesn't"             # ...or use double quotes instead
string3 = 3 * 'un' + 'ium'      # 3 times 'un', followed by 'ium'
string4 = 'Py' 'thon'           # Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

print(f"Strings can be enclosed in sigle quotes \'\'")
print(f"Use \\ to escape the single quote \'")
print(f"You can use double quotes instead \"doesn't\"")
print(f"\"Yes,\" they said.'")
print(f"\"Yes,\" they said.")
print(f"Isn\'t, they said.")
print(string3)
print(string4)
