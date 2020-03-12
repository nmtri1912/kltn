from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras

app = Flask('stock_pricer')


#-----

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np
from pickle import load
from numpy import argmax

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

model = load_model('model.h5')
#model.summary()

#clean data


# load a clean dataset
def load_clean_sentences(filename):
	return load(open(filename, 'rb'))
 
# load datasets
dataset = load_clean_sentences('english-german-both.pkl')
train = load_clean_sentences('english-german-train.pkl')
test = load_clean_sentences('english-german-test.pkl')

# fit a tokenizer
def create_tokenizer(lines):
	tokenizer = Tokenizer()
	tokenizer.fit_on_texts(lines)
	return tokenizer

def max_length(lines):
	return max(len(line.split()) for line in lines)

# prepare english tokenizer
eng_tokenizer = create_tokenizer(dataset[:, 0])
eng_vocab_size = len(eng_tokenizer.word_index) + 1
eng_length = max_length(dataset[:, 0])
print('English Vocabulary Size: %d' % eng_vocab_size)
print('English Max Length: %d' % (eng_length))
# prepare german tokenizer
ger_tokenizer = create_tokenizer(dataset[:, 1])
ger_vocab_size = len(ger_tokenizer.word_index) + 1
ger_length = max_length(dataset[:, 1])
print('German Vocabulary Size: %d' % ger_vocab_size)
print('German Max Length: %d' % (ger_length))


def encode_sequences(tokenizer, length, lines):
	# integer encode sequences
	X = tokenizer.texts_to_sequences(lines)
	# pad sequences with 0 values
	X = pad_sequences(X, maxlen=length, padding='post')
	return X

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

# generate target given source sequence
def predict_sequence(model, tokenizer, source):
	prediction = model.predict(source, verbose=0)[0]
	integers = [argmax(vector) for vector in prediction]
	target = list()
	for i in integers:
		word = word_for_id(i, tokenizer)
		if word is None:
			break
		target.append(word)
	return ' '.join(target)
#----

@app.route('/')
def show_predict_stock_form():
    return render_template('predictorform.html')
@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
       #model = get_model() #you can use pickle to load the trained model
        year = request.form['year']
        #predicted
        tk2 = create_tokenizer(year)
        year = year.split(" ")
        predicted = list()
        for text in year:
            tk = create_tokenizer(text)
            source = encode_sequences(tk,ger_length,text)
            temp = predict_sequence(model,eng_tokenizer,source) + ' '
            predicted.append(temp)

        predicted_stock_price = predicted

        #
        return render_template('resultsform.html', year=year, predicted_price=predicted_stock_price)


app.run("localhost", "9999", debug=True)