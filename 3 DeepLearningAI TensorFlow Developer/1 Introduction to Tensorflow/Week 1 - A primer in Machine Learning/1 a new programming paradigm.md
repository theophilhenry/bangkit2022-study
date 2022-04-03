<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## A primer in Machine Learning <hr/>
Answer + Data = Rules

We programmer, we have bunch of example we want to see, and have the computer figure out the rules.

Opens up possibilities that isn't feasible before. 

## Hello world of Neural Network <hr/>
This code in Python, Tensorflow, and API in Tensorflow 'Keras'

Keras makes easy defining neural networks. <br>
Neural network is set of function that can learn patterns.

```python
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# Dense = Layer of Connected Neurons
# 1 Unit, single neurons
# Succesive layers defined in sequence, hence Sequential

# Define what's input to the neural network in the first (ex: 1)
```

### At Keras, a lot of math implemented in function
`loss` and `optimizers`
```python
model.compile(optimizer='sgd', loss='mean_squared_error')
# sgd = stochastic gradient descent
```

Think of it this way,<br>
The neural network has no idea the relationship between X and Y, so it makes a guess. It will then measure how good/how bad the guess was. 

`loss` : Measure that, then gives the data to the `optimizer` which figures out the next guess. The opzimizer think how good or bad the guess using the data from the loss function.

Each guess should be better. as Accuracy gets to 100%, the term is `Convergence`.

### The Data
```python
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
```

### The Training
```python
model.fit(xs, ys, epochs=500)
# We ask the model how to fit the x values to the s values
# Epochs means it will go through the training loop 500 times.
```

### Finished Training
When the model finished training, we can give back values using the Predict method.
When given a 10, it returns number close to 19. Why? 
1. We train it using a very little data
2. Neural Network deal with probabilities. You need to adjust how you handle answers to fit. 

## Working through 'Hello World' Tensorflow and Python
