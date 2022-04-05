<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Multiclass Classifications <hr>
Dataset Source : <https://laurencemoroney.com/datasets.html#google_vignette>

What changes from binary classifier?
- on method flow_from_directory (ImageDataGenerator), set class_mode='categorical', instead of binary.
- on the last model, set dense layer output classifier to 3 layer, and activation to 'softmax'. Softmax will have probability, the output is the biggest probability.
- on the model.compile, change the loss='categorical_crossentropy'.

The return of predict method is `1-0-0`. The classes comes from the directory name 'papper', 'rock', 'scisors' (Alphabetical Order).