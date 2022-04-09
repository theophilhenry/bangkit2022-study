<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Word Embeddings <hr>
See the meaning sentiment of a corpus.

## IMDB Dataset <hr>
We have TFDS to get data that already available in Tensorflow. 

```python
import tensorflow as tf
print(tf.__version__) # See version of TensorFlow

import tensorflow_datasets as tfds
imdf, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True) # Returns data and metadata

import numpy as np
train_data, test_data = dmdb['train'], imdb['test'] # 25k data training, and 25k data testing

training_sentences = []
training_labels = []
testing_sentences = []
testing_labels = []

for s, l in training_data:
    training_sentences.append(str(s.numpy())) # The value are tensors, numpy actually extrating the value
    training_labels.append(str(l.numpy()))
for s, l in testing_data:
    testing_sentences.append(str(s.numpy()))
    testing_labels.append(str(l.numpy()))

# When training, labels are needed to by numpy array
training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)

vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type = 'post'
oov_tok = '<OOV>'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(training_sentences)
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, maxlen=max_length, truncating=trunc_type)

testing_sequences = tokenizer.text_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, maxlen=max_length)

model = model.keras.Sequential([
    # Embedding is the key to text sentiment analysis in Tensorflow
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    # Flatten -> 6 Dense relu -> 1 Dense sigmoid 
])

model.compile(loss=, optimizer=, metrics=)
model.summary()

num_epochs = 10
model.fit(padded, 
          training_labels_final,
          epochs=num_epochs,
          validation_data=(testing_padded, testing_labels_final))
```

### More about embedding
Say the word dull and bad, often comes out in a negative review. So,, they are close to each other in the sentences! thus their vector will be similar.

While `training`, the `model` can learn these vector, `associating` them with the `labels`, to come up with `embbeding` (the vector for each word with their associated sentiment)

Result of embedding is 2D array with the length of the sentences and the embedding dimension (ex: 16). That's why we need to flatten it.

Sometimes, we don't use flatten. We can instead do Global Average Pooling 1D. The reason is the size of output fed into the dense layer. It averages accross the vector to flatten it out. 

### Visuializing Embedding
```py
e = model.layers[0] # Get the output of the embedding layers
weights = e.get_weight()[0]
print(weights.shape) # Shape : (vocab_size, embedding_dim)
# Output (10000, 16)

# To be able to plot, reverse the word index, now the key is number, and the value is the word.
reverse_word_index = tokenizer.index_word

# Write the vectors and the metadata into files
import io
# More info about this, open the C3_W2_Lab_1_iomdb.ipynb
```

To reender the result, open <projector.tensorflow.org>. You can load data, and load the `.tsv` data and meta on each.
Click the sphere data on top left.

