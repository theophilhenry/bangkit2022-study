<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Pro-tokenized Words <hr>
IMDb dataset has pre-tokenized for you, but the tokenization is done on sub words. Sequence of words can be as important as their existences.

```py
imdf, info = tfds.load("imdb_reviews/subwords8k", with_info=True, as_supervised=True) # Returns data and metadata as pre-tokenized
train_data, test_data = imdb['train'], imdb['test']
tokenizer = info.features['text'].encoder # Subword Tokenzer ( SubwordTextEncoder )

# Shape comes from the sub_word tokenizer cannot be easily flatten,
# so use GlobalAveragePooling1D() for it's flattening layer.
```

Subwords usually meaningless. But when you put them into sequence, that's when they have meaningful semantics. Learning from sequences would be a great way! Next we'll learn recurring neural network.