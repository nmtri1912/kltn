import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.model_selection import train_test_split

import unicodedata
import re
import numpy as np
import os
import io
import time

datapath = "data/train-en-vi/"

#read data
with open(datapath+"train.en", 'r', encoding='utf-8') as f:
    linesEN = f.read().split('\n')

with open(datapath+"train.vi", 'r', encoding='utf-8') as f:
    linesVI = f.read().split('\n')

trainEN = [] #data clean
trainVI = [] #data clean

def preprocess_sentence(w):
    return '<start> ' + line + ' <end>'

lenData = 0
count = 1

for line in linesEN:
    if len(line) > lenData:
        lenData = len(line)

for line in linesEN:
    if len(line) == lenData or len(line) >= 700:
        print(count)
    count+=1

print(lenData)

"""
for line in linesEN:
    if len(line) < 50:
        temp = '<start> ' + line + ' <end>'
        trainEN.append(temp)

for line in linesVI:
    if len(line) < 50:
        temp = '<start> ' + line + ' <end>'
        trainVI.append(temp)



trainEN = trainEN[0:30000]
trainVI = trainVI[0:30000]

def max_length(tensor):
    return max(len(t) for t in tensor)

def tokenize(lang):
    lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
    lang_tokenizer.fit_on_texts(lang)

    tensor = lang_tokenizer.texts_to_sequences(lang)

    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')

    return tensor, lang_tokenizer

def load_dataset(trainEN, trainVI, num_examples=None):
    # creating cleaned input, output pairs
    inp_lang = trainEN
    targ_lang = trainVI

    input_tensor, inp_lang_tokenizer = tokenize(inp_lang)
    target_tensor, targ_lang_tokenizer = tokenize(targ_lang)

    return input_tensor, target_tensor, inp_lang_tokenizer, targ_lang_tokenizer

# Try experimenting with the size of that dataset
num_examples = 30000
input_tensor, target_tensor, inp_lang, targ_lang = load_dataset(trainEN, trainVI, num_examples)

# Calculate max_length of the target tensors
max_length_targ, max_length_inp = max_length(target_tensor), max_length(input_tensor)

# Creating training and validation sets using an 80-20 split
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.2)

# Show length
print(len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val))

def convert(lang, tensor):
    for t in tensor:
        if t!=0:
            print ("%d ----> %s" % (t, lang.index_word[t]))


print ("Input Language; index to word mapping")
convert(inp_lang, input_tensor_train[0])
print ("Target Language; index to word mapping")
convert(targ_lang, target_tensor_train[0])
"""

"""
#create dataset
BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
steps_per_epoch = len(input_tensor_train)//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word_index)+1
vocab_tar_size = len(targ_lang.word_index)+1

dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)

example_input_batch, example_target_batch = next(iter(dataset))
example_input_batch.shape, example_target_batch.shape

"""