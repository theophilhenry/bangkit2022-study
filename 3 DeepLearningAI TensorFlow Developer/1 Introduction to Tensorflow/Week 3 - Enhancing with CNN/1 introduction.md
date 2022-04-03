<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## What are Convolutions and Pooling? <hr/>
One of the things that you would know from previous pattern recognition, is the images have a wasted spaces. 

784 pixel, it would be interseting if we could condense the image down to the `important features`.

### Convoutions? 
If you done image processing, it usually involves filters over the image. For every pixel, take it's value and it's neighboor's value. If our filter 3x3, we take a look at the immedeate neighboor.

To get the `new value` of that 3x3, we `multiply` each neighboor, by the corresponding value in the filter. And then `add` all of them up.

That's `Convolution`!

> The idea is that some convolutions will change the image in some way, that certain features in the image get emphazied.

### Combine with `Pooling`?
Pooling is a way of compressing an image. Quick way to do this is : 
- go over the image of four pixels at a time, I.E the current pixel and its neighbors underneath, and to the right of it. Out of that 4, pick the biggest value. (Another way of saying, is take a look at 2x2 grid)

This will preserve the feature that were highlighted by the convolution, while simultaneously quartering the size of the image.

<br>

## Implementing Convolutional Layers <hr>
```python
model = keras.model.Sequential([
    keras.layers.Conv2D(
        64, # Generate 64 filters, 
        (3,3), # Filters are 3x3
        activation='relu', # Negative val will be thrown
        input_shape=(28,28,1) # 28x28, extra 1 : telling it we're using a single byte for color depth
    )
    # Why 64? They start with a set of known good filters, the one that work from that set, are learned over time.


    keras.layers.MaxPooling2D(2, 2), # Creates a pooling layer
    # 2x2, from 4 pixel, the biggest one will survive.

    # We add another conv layer and pooling layer
    # So that the network can learn another set of convolution on top of the existing one. and pool it again to reduce the size.
    keras.layers.Conv2D(64,  (3,3),  activation='relu',  input_shape=(28,28,1)
    )
    keras.layers.MaxPooling2D(2, 2),
    # Last 3 are the same
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax'),
])
```

### Useful method
`model.summary()` : Inspect the layers of the model, and see the journey of the image through convolutions. 

<br>

## Walking Through Convolutions <hr>
