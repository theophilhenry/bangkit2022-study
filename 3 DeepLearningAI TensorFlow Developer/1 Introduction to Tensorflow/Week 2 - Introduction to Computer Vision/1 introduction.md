<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## An Introduction to Computer Vision <hr/>
```python
fashion_mnist = tf.keras.datasets.fashion_menist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

Btw, the train_labels for ankle boot is 09. Why isn't "Ankle Boot"?<br>
It is for `Bias Prevention`. This is to reduce bias. If we use english, we bias towards the english speakers.

## Coding Computer Vision Neural Network <hr/>
```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax),
])
```

The `first` layer is flatten layer, with input shape 28x28. We expect the shape of the data to be in. Flatten takes this 28x28 square, and turns it into a simple `linear array` (1D Array).

The middle/`hidden` layer has 128 neurons. Think of it as variables in a function. It will predict the weight.

The `last` layer has 10 neurons in it. Because we have 10 class of clothing in dataset.

## Walk through a Notebook for Computer Vision <hr/>
Our data have the range values from 0-255, but Neural Networks work better with `normalize` data.
Change it into 0-1, by dividing every value by 255.
```python
training_images = training_images / 255.0
test_images = test_images / 255.0
```

Evaluating the model
```python
model.evaluate(test_images, test_labels)
# [loss, accr], 
```

## Using Callbacks to Control Training <hr/>
How to stop training when reaches a certain accuracy or etc...

In every Epoch you can callback to a code function! 

`logs` : Buncho information about the current state of training. 

`on epoch end` is good practice to do, because with some data and algoriuthms, the loss my vary up/down during the epoch because all the data hasn't yet been processed. 

