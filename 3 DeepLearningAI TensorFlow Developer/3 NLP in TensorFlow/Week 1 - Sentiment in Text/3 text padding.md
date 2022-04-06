<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Padding <hr>
Before you can train with texts, we needed to have some level of `uniformity` of `size`,

```python
from tensoflow.keras.preprocessing.sequence import pad_sequences

padded = pad_sequences(sequences)
```

Putting zeros before the sentences, up to the max sentence's length.

Want the padding after? add param pad_sequences(..., `padding`='post')

You notice the width of padding, is the same as the longest sentences. We can overwrite it with `maxlen`=5 param. We want our sentences to have a maximum of five words.

But, what if we have maxlen, and there's sentences that longer than the 5 word, we'll lost the sentences right? But from where? Like the sentences default to 'pre', we'll lose the beggining of the sentences. To override that, use `truncating`='post'

