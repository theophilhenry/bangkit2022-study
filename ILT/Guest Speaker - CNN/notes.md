<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

# Convolutional Neural Network : Concept and Implementation
__By Vincent Tatan__<br>
Sr. Machine Learning Engineering/Analyst Google
<hr>

## Google : Trust and Safety
To find pishing. Google Chrome will have a warning. You package all of it in ML Pipeline.

Today we'll learn how to predict an image.

## Agenda
1. Machine Learning in Image Recognition
2. Priciples in CNN : Convolition, ReLU, Max Pooling
3. CNN stacks + Fully Connected Layer
4. Avoid Overfitting (Dropout and Image Augmentation)
5. Transfer Learning

## 1. Machine Learning in Image Recognition <hr>
In traditional programming, we look at the traditional features (cat : black color, sharp ears).

## 2. Priciples in CNN <hr>
Type of neural network compromising of different layers of convolitions and max pooling mainly for image recognition.
1. Convolution 
2. ReLU Activation 
3. Max Pooling 

Interchangable to Sigmoid and Average Pooling

Young Lady / Old Lady? <br>
We recognize by relying on : 
- Data (strokes of painting)
- Prior Knowledge (understanding of faces)

Notice in a grayscaled, 1/0 color (black/white), a pattern can be seen.

### What is Convolution?
Convolution is everywhere.

Ex : 
- There's a filter in instagram, artistic filter, b&w filter. Right?

The idea is we can take a kernel and image, transform it into a transformed image.

### How does it works?
`[1,1,1,1,0,0]`<br>
Which order of the element where I see there's a change from 1 to 0?
[1,1,1,`1,0`,0] <- at the index 3, it changes 1 0
Answer is
[0,0,0,1,0,0]

You do that with dot operation between a kernel
```
[ 1 1 1 1 0 0 ] [ 1 -1 ]
1st : 1*1 + 1*-1  = 0
2nd : 1*1 + 1*-1  = 0
3rd : 1*1 + 1*-1  = 0
4th : 1*1 + 1*-0  = 1
5th : 0*1 + 0*-1  = 0
```

### Activation Function ReLU
ReLU : common and popular activation function in Neural Network.

we use ReLU because
- first, it is very simple. Everything below 0 is 0, everything on top of that is that number.
- second, it is not a linear function.
- finally, ReLU mimics our pain.

### Max Pooling (2-D)
We are trying to reduce the feature map. 

2x2, with strides 2. 
nyamping ke kanan 2 kali, trs diliat 2x2. Diliat maximumnya.

This product the highest impact, and reduces the risk of overfitting.

Analogy :
Imagine the best car. Think about it! <br>
- Do you still remember the one who wear dress have pimples?
In your mind, you think about the car. If you ask about something that's not important. Who is the driver,we don't know right. Max Pooling find the most important.

Why we pick the maximum number with ReLU? And does the matrix that we process in ReLU, is the intensity of color?

## 3. CNN Stacks + Fully Connected Layers
How can we generate real results.

Convolution : We take the important piece
SubSampling : Max Pooling
Squash all the component into each individual neurons.

5x5 feature map, 25 neurons, do ANN with it.

A curve important? Tune it up!

### Fully Conected Layer Activation : Softmax / Sigmoid
Softmax : Squashes the probabilty score to add up to 1.0.
Forward propagation -> feedforward output
```
cat dog horse
5   4   2
4   2   8
4   4   1

cat     dog     horse
0.71    0.26    0.04    = 100.01%. Huh? Sigmoid never 100%.
0.02    0.00    0.98
0.49    0.49    0.02

Sigmoid on crack.
```

## Using Tensorflow + Keras <hr>
```python
from tensorflow.keras.models import Sequential
from tensofrlow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import np
import plt
```

```python
# We create CNN Stacks
model = Sequential([
    Conv2D(), MaxPooling, ...
    # Fully Connected Layer
    Flatten(),
    Dense(512, activation='relu')
    Dense(1, activation='sigmoid') # Density like above cat/dog/horse
])
```

```python
# We want to have the few lost ass possible.
# We want keep changing the kernel (prior knowledge)
# Back/Forward propagation make each step a training
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) # Change to 'categorical_crossentropy' for SoftMax
```

### Training our CNN
```python
history = model.fit_generator([
    train_data_gen,
    steps_per_epoch=total_
    ...
])
```

Whenever you see the accuracy, there's a gap in training in testing. It memorizes to much from the training data. 

It basically look to the one feature.

teachablemachine.withgoogle.com/train/image

## Avoid Overfitting <hr>
| Common Mistakes | Solutions |
| - | - |
| Using test as the valiaditon set to test the model | Use validation sets as validation tests and test models as final tests (Watch this again 01:01:00) |
| Dataset is relatively small | Image augmentation to add new variant of images |
| Over Memorization | Dropout/Reduce epoch/layer/neurons per laer to increase generalizations |

### Data Augmentation
Crop, Flip, Zoom, Flips.

### Dropout
Drop neurons, why?<br>
Analogy : <br>
When we go to BANK, we talk to a different teller. We only want to talk to IGA? NOO,  we always talk to the different person right!?

We prevent collution. To prevent heist! We don't want the criminal know many things. 
The bank will rotate. 
You don't want the neurons to know each other. We want to know just enough to be creative with the output.


## Transfer Learning
Leverage PreTrained Model by Experts

How we can improve more?

Why don't we reuse expert trained model?

Does transfer learning means we just copy the same architechture? Or we take the model that already have been trained before (with the expert data), and we train it even more?

VGG Params are HUGE! It would take hours! 
What you do, is we don't want to train on VG-16.
```python
conv_base.trainable = False
```


1. How do define the kernel of the prior knowledge size?<br>
    Actually we dont define the kernel. Neural network depends on the prior knowledge. 

2. How to create a CNN Layers?<br>
    We have a starting formula. but that's not really many kinds of phylosophy.

    Always start with a simpler model. If it's underfitting, do more layer.

3. Advantages between droping a layer between tuning the number of neurons?<br>
    No staturation from the start. 

4. Dilema
    Just do dropout whenever there's an overfitting. 

5. Why don't we use big number of layer from the start i.e 16, 32, 64?<br>
    The Idea is we want to solve step-by-step. Iterate through trial-and-error. Make sure you start small. We can hypertune it later. 

6. Determine which pre-trained model is suitable?<br>
    Depends. Guideline :
    - Not all pre-trained model fit the same. Use cases! Some pre-trained model build on landmark. Like monas, candi, all landmarks. Some other model are trained on top of furnitures. You don't need a complex modle. 
    - What it is trained on.
    - Memory Complexity. We trained VGG-19 everytime open android phone, how come the battery dies so fast. Why we use YOLO ? Single shot detector very fast. Trade off between accuracy and speed.

7. Accuracy OR Recall?<br>
    When we talk about percision, what model we are dealing with. in F1 Score.

    For everything that is very sensitive to how model is accurate, do percision! Health like Cancer, HIGH PERCISSION. 

    Recall, which positive situation. Covid? PCR and Swab and AntiGen. We just care about the cost. Whether this person really really have covid, PCR right? Precission. SWAB : recall (spread the net as much as possible).

8. Can CNN identify an object in an extreme object?
    Depends on the data. 

9. "Input Ran Out of Data" Warning
    I'm not really sure about this. Usually doesn't get an error. It might happen. Maybe there is a statistical validations. 


10. DevOps vs MLOps
    DevOps : Look into an operational aspect. Past is so slow to do something and the customer needs. DevOps is a movement. Make feature fast and develop faster. Like CI and CD.

    MLguy : How to build the model with the best accuracy
    MLOps : Make things happen

    What if we put in data in DevOps. PS1 10 years ago, and PS1 today. It still work the same right? 
    Gojek, does gojek works the same way? Because the data changes, model changes, behavior changes. ML recognize, and do a statistical analytic. Launch ML that's reliable, and use in a stable manner. And FAST.

vintatan@google.com (WOW A GOOGLE EMAIL)


