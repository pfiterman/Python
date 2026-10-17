# NLTK is a huge library and it is inadvisable to import all its packages and subpackages. 
# If you examine the code, you will realize that only the required functionalities from the subpackages such as corpus and tokenize are imported within the code.
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# The first function used is word_tokenize(). This takes the text and produces the first part of the output in which the words are tokenized, 
# meaning they are separated into individual components, including punctuation and contractions (e.g., splitting "industry's" into ["industry", "'s"]).
print(word_tokenize(text)) 
# ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.']

# While the same can be done with the split() function from the string class, word_tokenize() is more suitable for natural language processing 
# because it handles linguistic nuances more effectively.

# The second function sent_tokenize() tokenizes the block of text into sentences, producing the second part of the output.
print(nltk.tokenize.sent_tokenize(text))

# For the third output, the code removes what are called "stopwords" from the text. 
# Stopwords are common words in English, such as "a," "the," and "him," which can be considered redundant for many natural language processing tasks. 
# These words are retrieved using stopwords.words("english"). 
# A for loop is then used to filter out these stopwords and create a new list called new_text. 
# The difference between the first and the final outputs illustrates the removal of stopwords, which leaves only the more significant words in the text.
stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)