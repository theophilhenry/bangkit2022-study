<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Text to sequence <hr>
Next we want to change our corpus to a lists of values based on these tokens.

After that, manipulate these lists, not least to make every sentence the same length, otherwise it will be hard to train NN with them.

```python
# Will change the word in our sentences to its corresponding token
sequence = tokenizer.texts_to_sequences(sentences)
print(sequences)
# Output : 
# [[4, 2, 1, 3], [4, 2, 1, 6] ...]
```

Btw, texts_to_sequences can take any kind of sentences!
What happen to the unseen one? It will not be added to the sequence!

What we know?
- We need a lot of data, to get a broad vocabolary
- Instead of ignoring words, it is better to put a special value in it. Do property in a tokenizer.

```python
tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
```
`oov_token`: Out of Vocabolary token, we set it to "<OOV>". Use anything you like, but must be distinct with real word.
The OOV will get tokenize, for example { <OOV> : 1, ... },
So next time in the test corpus, each out of vocab words will be replaced with that value.

