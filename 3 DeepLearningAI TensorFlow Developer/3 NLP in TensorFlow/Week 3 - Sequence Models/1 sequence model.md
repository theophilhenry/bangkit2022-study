<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>


## Sequence Model <hr>
RNN is one example of sequence model. Find out more about it in <https://www.coursera.org/lecture/nlp-sequence-models/deep-rnns-ehs0S> course.


## Sequence Model Limitation <hr>
LSTM removes that limitaton, by using cell state context. This keep context from earlier tokens relevance, in later ones.

Cell state is bidirectional. Later context can impact earlier ones.

Learn more about LSTM here <https://www.coursera.org/lecture/nlp-sequence-models/long-short-term-memory-lstm-KXoay>

LSTM : words that aren't immediate neighbors can affect each other's context.

## Adding LSTM <he>
```python
model = ...
    ...Embedding
    # The param is the output desired from that layer. 
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64))
    # When you wrap with bidirectional. the output will be twice as big.
    ...Dense
```
### You can also stack it.
```python
model = ...
    ...Embedding
    # Make sure to return sequences, this ensures the outputs of the LSTM
    # match the desired input of the next one
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True))
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32))
    ...Dense
```

### Tips reading Accuracy Measurement
Jagged lines : model needs improvement

For more epoch, only 1 embedding layer is prone to sharp accuracy drop.

