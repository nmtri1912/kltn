import keras, tensorflow
from keras.models import Model
from keras.layers import Input, LSTM, Dense
import numpy as np

batch_size = 64
epochs = 100
latent_dim = 256

#Encoder
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
encoder_states = [state_h, state_c]

#Decoder
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                                     initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

#Model
model = Model(inputs=[encoder_inputs, decoder_inputs], 
              outputs=decoder_outputs)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.summary()