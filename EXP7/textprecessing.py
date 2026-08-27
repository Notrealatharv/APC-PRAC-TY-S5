# '1. What is Tokenization?
# Tokenization means breaking text into smaller pieces called tokens.'

'2. Word Tokenization'

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text = "I love Python programming."
words = word_tokenize(text)
print(words)

'3. Sentence Tokenization'
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt_tab')
text = "I love Python. Python is easy to learn. I am studying NLP."
sentences = sent_tokenize(text)
print(sentences)

'4. Word + Sentence Tokenization Together'

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab')

text = "I love Python. Python is easy to learn."

# Sentence Tokenization
sentences = sent_tokenize(text)

print("Sentences:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)

print("Words:")
print(words)

################################################################

# STOPWORD REMOVAL
'1. Stop Word Removal using NLTK'

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

text = "I am learning Python in college."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Words:")
print(words)

print("After Stop Word Removal:")
print(filtered_words)

###################################################################

# STEMMING
'1. Stemming Using NLTK'
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "studies", "studying", "running"]

for word in words:
    print(word, "->", stemmer.stem(word))


'2. Stemming a Sentence'
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

text = "The students are studying and playing games."

words = word_tokenize(text)

stemmer = PorterStemmer()

for word in words:
    print(word, "->", stemmer.stem(word))

'3. Stemming with Stop Word Removal'
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

text = "I am studying Python and playing games."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

for word in words:
    if word.lower() not in stop_words and word.isalpha():
        print(word, "->", stemmer.stem(word))