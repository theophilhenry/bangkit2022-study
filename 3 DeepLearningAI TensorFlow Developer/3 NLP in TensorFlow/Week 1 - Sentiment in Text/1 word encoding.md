<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Word based encoding <hr>
We can take ASCII Value, but will it help us to understand the meaning of that word?
`LISTEN` : 076 073 081 084 069 078
Semantic in word anrent arent encoded in letters.
`SILENT` : Different meaning ,but the same letter!

How about words? The value doesn't matter. But per word have a unique idenfitifer.
`I love my dog` :
I = 001
love = 002
my = 003
dog = 004

I love my cat : 001 002 003 005
cat = 005

We can begin to see similarities in sentences.

## Using API
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'I love my dog',
    'I love my cat',
]

# Tokenizer instance, num words, because there are only 5 word. But based on lots of text, so by setting the hyper parameter, tokenizer wil ltake top 100 words by volume, and encode those.
# The impact of less words can be minimal and training accuracy, but huge in training time.
# Just give me the most common 100 words in the entire corpus.
tokenizer = Tokenizer(num_words = 100)

# Takes in the data, and tokenize it
tokenizer.fit_on_texts(sentences)

# The tokenizer returns dictionary, key : word, value : token of that word.
word_index = tokenizer.word_index
print(word_index)
# Sample result : {'i' : 1, 'my': 2, ... }
# It's automatically default to lowercasing
# It's also strip punctuation and grammar out
```