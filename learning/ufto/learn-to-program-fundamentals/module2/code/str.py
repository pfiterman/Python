# Valid str operations
str1 = "hello"
str2 = "how are you?"
str3 = "short- and long-term"
sunny_greating = "What a beautifu day!"
storm_greeting1 = "Wow, you're dripping wet."
storm_greeting2= 'Wow, you\'re dripping wet.'
concat1 = 'personal' + 'penguin'
concat2 = 'I want to be your personal ' + 'penguin' + '!'
puzzle_start = 'I want to be your personal '
punctuation = '!'
noun = 'earthworm'
puzzle = puzzle_start + noun + punctuation

repeat = 'ha' * 5 #'hahahahaha'
exp1 = 'Bwa' + 'ha' * 5 #Bwahahahahahaha
exp2 = ('Bwa' + 'ha') * 5 #BwahaBwahaBwahaBwahaBwaha

# You can't convert float to str implicitly
'My shoe size is ' + 8.5  #TypeError: Can't convert 'float' object to str implicitly 

# You can't multiple str
'ha' * '5' # Can't multiply sequence by non-int of type 'str' 

# You can't use different operators to str
'a' - 'b'  # TypeError: Unsupported operand type(s) for -: 'str' and 'str'
'a' / 'b'  # TypeError: Unsupported operand type(s) for /: 'str' and 'str'
'a' ** 'b' # TypeError: Unsupported operand type(s) for ** or pow(): 'str' and 'str'