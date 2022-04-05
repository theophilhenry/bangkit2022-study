<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Transfer Learning <hr>
Rather than training from stratch. We can download open source trained model that has been trained for big dataset.

We can download it, set it to trainable and freeze or lock to those layers.

<br>

## Understanding the Concepts <hr>
The problem from the previous dataset is overfitting because the training data is small. What if we can download model, and use the features of that model?

We don't always have to import all the layers inside. 

### Coding Transfer Learning from the Inception Model
See [python file](transfer_learning_inception.ipynb)

After we use transfer learning, there's another case of overfitting, which the validation accuracy get's down BAD! To fix that we can use `Dropout`

<br>

## Dropout <hr>
More info : <https://www.youtube.com/watch?v=ARq74QuavAo>
`dropout` : Remove a random number of neurons in neural network.

Why?
1. `Neighbooring neurons` often end up with `similar weights`, which leads to overfitting
2. Often a `neuron` can `over-weigh` the `input` from a neuron in the `previous` layer, and can over specialize as a result.

### Exploring Dropouts
```python
# The param is between 0-1
# It's the fraction of units to drop. 
# In this case we're dropping 20% of our neurons.
x = layers.Dropout(0.2)(x)
```