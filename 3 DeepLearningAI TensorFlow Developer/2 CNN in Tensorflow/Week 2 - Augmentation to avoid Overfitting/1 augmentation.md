<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Augmentation <hr>
Sometimes we don't have access to a lot of dataset. We will create a new data, with augmented the image, such as rotate, skew. 

Important trick, to not take an image, and blow up the memory requirement.

The idea is that you're `not` going to `edit` the images `directly` on the `drive`. As they get float off the directory, then the augmentation will take place in memory `as` they're being `loaded` into the neural `network` for training

Image can be streamed to the training, thus will not overwrite with a lot of augmentation.

## Let's get started
Dataset small = Few examples = Classification mistakes

```python
train_datagen = ImageDataGenerator(
    rescale = 1./255, # Resacling the output
    rotation_range=40, # 0-180 degree random rotation
    
    # Shifting : Move the image around inside it's frame.
    # Randomly move the subject around. 20% shifting vertically or horizontally.
    width_shift_range=0.2, 
    height_shift_range=0.2,

    shear_range=0.2, # Sheering along the x axes, shear up to 20% of the image.

    zoom_range=0.2, # Zoom random amount up to 20%

    horizontal_flip=True, # Random horizontal flipping

    fill_mode='nearest' # Fills in pixel might loss in the operation lkike shear. To keep the pixel uniformly.
)
```

### Exploring Augmentation with Horses and Humans
Bear in mind that you don't just need a broad set of images for training, you also need them for testing or the image augmentation won't help you very much. 

