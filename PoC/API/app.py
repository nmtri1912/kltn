import keras.backend.tensorflow_backend as tb
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from numpy import argmax
from pickle import load
import numpy as np
from keras.models import load_model
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow import keras

app = Flask('stock_pricer')

# -----

tb._SYMBOLIC_SCOPE.value = True


sess = tf.compat.v1.Session()
graph = tf.compat.v1.get_default_graph()

# model.summary()

# clean data


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
    with sess.as_default():
        with graph.as_default():
            prediction = model.predict(source, verbose=0)[0]
            integers = [argmax(vector) for vector in prediction]
            target = list()
            for i in integers:
                word = word_for_id(i, tokenizer)
                if word is None:
                    break
                target.append(word)
            return ' '.join(target)
# ----


@app.route('/')
def show_predict_stock_form():
    # return render_template('predictorform.html')
    return render_template('try.html')
    # return "hello"


@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        with sess.as_default():
            with graph.as_default():
                model = tf.keras.models.load_model("model.h5")
                inputGerman = request.form['input']
                tk2 = create_tokenizer(inputGerman)
                inputGerman = inputGerman.split(" ")
                predicted = str()
                for text in inputGerman:
                    tk = create_tokenizer(text)
                    source = encode_sequences(tk, ger_length, text)
                    temp = predict_sequence(model, eng_tokenizer, source) + ' '
                    # predicted.append(temp)
                    predicted = predicted + temp + ' '
                    predicted = predicted[:-1]

                predicted_stock_price = predicted

        #
        return render_template('resultsform.html', german=inputGerman, predicted_price=predicted_stock_price)


@app.route('/translate', methods=['POST'])
def translate():
    # print(request.form['input'])
    # return {'message': 'fail to request'}, 200
    if request.method == 'POST':
        with sess.as_default():
            with graph.as_default():
                model = tf.keras.models.load_model("model.h5")
                inputGerman = request.form['input']
                tk2 = create_tokenizer(inputGerman)
                inputGerman = inputGerman.split(" ")
                predicted = str()
                for text in inputGerman:
                    tk = create_tokenizer(text)
                    source = encode_sequences(tk, ger_length, text)
                    temp = predict_sequence(model, eng_tokenizer, source) + ' '
                    predicted = predicted + temp + ' '

                predicted = predicted[:-1]
                predicted_stock_price = predicted

        return jsonify({'output': predicted}), 200


app.run("localhost", "9999", debug=True)
