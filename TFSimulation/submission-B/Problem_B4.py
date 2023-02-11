# ===================================================================================================
# PROBLEM B4
#
# Build and train a classifier for the BBC-text dataset.
# This is a multiclass classification problem.
# Do not use lambda layers in your model.
#
# The dataset used in this problem is originally published in: http://mlg.ucd.ie/datasets/bbc.html.
#
# Desired accuracy and validation_accuracy > 91%
# ===================================================================================================

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pandas as pd
import numpy as np



def train_val_split(sentences, labels, training_split):
    # Compute the number of sentences that will be used for training (should be an integer)
    train_size = int((len(sentences) * training_split))

    # Split the sentences and labels into train/validation splits
    train_sentences = sentences[:train_size]
    train_labels = labels[:train_size]

    validation_sentences = sentences[train_size:]
    validation_labels = labels[train_size:]

    return train_sentences, validation_sentences, train_labels, validation_labels


def fit_tokenizer(train_sentences, num_words, oov_token):
    # Instantiate the Tokenizer class, passing in the correct values for num_words and oov_token
    tokenizer = Tokenizer(num_words=num_words, oov_token=oov_token)

    # Fit the tokenizer to the training sentences
    tokenizer.fit_on_texts(train_sentences)

    return tokenizer


def seq_and_pad(sentences, tokenizer, padding, maxlen, trunctype):
    # Convert sentences to sequences
    sequences = tokenizer.texts_to_sequences(sentences)

    # Pad the sequences using the correct padding and maxlen
    padded_sequences = pad_sequences(sequences, maxlen=maxlen, padding=padding, truncating=trunctype)

    return padded_sequences


def tokenize_labels(all_labels, split_labels):
    ### START CODE HERE

    # Instantiate the Tokenizer (no additional arguments needed)
    label_tokenizer = Tokenizer()

    # Fit the tokenizer on all the labels
    label_tokenizer.fit_on_texts(all_labels)

    # Convert labels to sequences
    label_seq = label_tokenizer.texts_to_sequences(split_labels)

    # Convert sequences to a numpy array. Don't forget to substact 1 from every entry in the array!
    label_seq_np = np.array(label_seq) - 1

    ### END CODE HERE

    return label_seq_np

def solution_B4():
    bbc = pd.read_csv(
        'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/bbc-text.csv')

    # DO NOT CHANGE THIS CODE
    # Make sure you used all of these parameters or you can not pass this test
    vocab_size = 1000
    embedding_dim = 16
    max_length = 120
    trunc_type = 'post'
    padding_type = 'post'
    oov_tok = "<OOV>"
    training_portion = .8

    # YOUR CODE HERE
    sentences = []
    labels = []

    for index, document in bbc.iterrows():
        if index == 0:
            continue
        labels.append(document[0])
        sentences.append(document[1])

    # Using "shuffle=False"
    train_sentences, val_sentences, train_labels, val_labels = train_test_split(sentences, labels, train_size=training_portion, shuffle=False)


    # Fit your tokenizer with training data
    tokenizer = fit_tokenizer(train_sentences, vocab_size, oov_tok)

    # Add Padding
    train_padded_seq = seq_and_pad(train_sentences, tokenizer, padding_type, max_length, trunc_type)
    val_padded_seq = seq_and_pad(val_sentences, tokenizer, padding_type, max_length, trunc_type)

    # Tokenize Label
    train_label_seq = tokenize_labels(labels, train_labels)
    val_label_seq = tokenize_labels(labels, val_labels)


    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(6, activation='softmax')
    ])

    # Make sure you are using "sparse_categorical_crossentropy" as a loss fuction
    model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    history = model.fit(train_padded_seq, train_label_seq, epochs=100, validation_data=(val_padded_seq, val_label_seq))

    return model

    # The code below is to save your model as a .h5 file.
    # It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_B4()
    model.save("model_B4.h5")
