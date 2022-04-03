<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Using ImageDataGenerator <hr>
So far you use uniform images. 

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255) # Rescale to Normalize Data
train_generator = train.datagen.flow_from_directory( # Load images from that dir and its sub-dir
    # Don't only point the sub-directory, point at the dir!
    # The name of the sub-directories will be the labels for your images.
    train_dir,
    target_size=(300, 300) # Resize as they're loaded
    batch_size=(128), # The images will be loaded for training and testing in batches.
    class_mode='binary' # This is a binary classifier, pick between 2 things (horses and humans)
    # Other option will explore later.
)

test_datagen =  ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(val_dir, target_size=(300,300),batch_size=32,classmode='binary')
```

<br>

## Defining a ConvNet using Complex Images
For the model, the only difference are
- The input shape is  (300,300,3)
- There are 3 ConvLayers
- The output is 1, and activation is sigmoid (better on binary data) where one is 1 and the other is 0.


### Compiling the Model
```python
# Pick binary for binary problem.
# Adam optimizer? It is fun tu use RMSprop, where you can adjust the learning rate.
model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.0001), metrics=['accuracy'])
```

### Training the Data
Because you're using generator, not dataset. The fit will be different.
```python
history = model.fit(
    train_generator, # Streams images from training dir. Remember the batch?
    steps_per_epoch=8, # There are 1024 images, we load 128 at a time, In order to load them all, do 8 batches. 
    epochs=15,
    validation_data=validation_generator,
    validation_steps=8,
    verbose=2 # How much to display while training, 2 : less animation.
)
```

### Doing the Prediction
```python
import numpy as np
from google.colab import files
from keras.preprocessing import image

uploaded = files.upload()

for file_name in uploaded.keys():
    path = '/content/' + file_name
    img = image.load_img(path, target_size=(300, 300))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)

    print(classes[0])
    if classes[0] > 0.5 : print("{} is a human".format(file_name))
    else : print("{} is a horse".format(file_name))
```

<br>

## Walking Through the Dev a ConvNet <hr>




