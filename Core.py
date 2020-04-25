import os
import numpy as np
from pickle import dump
from keras import optimizers
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer


def readTokens():
    with open("data/preprocessed_data.txt", "r") as f:
        data = f.read()
    return data


def createModel(vocabularySize, seqLength):
    model = Sequential()
    model.add(Embedding(vocabularySize, seqLength, input_length=seqLength))
    model.add(LSTM(50, return_sequences=True))
    model.add(LSTM(50))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(vocabularySize, activation='softmax'))
    opt_adam = optimizers.adam(lr=0.001)
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt_adam, metrics=['accuracy'])
    model.summary()
    return model


text = readTokens()
token = text.split()

train_len = 4
text_squence = []

for i in range(train_len, len(text)):
    seq = token[i-train_len:i]
    if seq and len(seq) >= 4:
        text_squence.append(seq)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_squence)
sequence = tokenizer.texts_to_sequences(text_squence)

vocabularySize = len(tokenizer.word_counts)

sequence_matrix = np.empty([len(sequence), train_len], dtype='int32')

for i in range(len(sequence)):
    sequence_matrix[i] = sequence[i]

training_data = sequence_matrix[:, :-1]
train_targets = sequence_matrix[:, -1]

train_targets = to_categorical(train_targets, num_classes=vocabularySize+1)
seqLength = training_data.shape[1]

model = createModel(vocabularySize+1, seqLength)
path = os.path.join('checkpoints', 'model.h5')

checkPoint = ModelCheckpoint(
    path, monitor='loss', verbose=1, save_best_only=True, mode='min')

model.fit(training_data, train_targets, batch_size=128,
          epochs=700, verbose=1, callbacks=[checkPoint])

dump(tokenizer, open(os.path.join('pickle_objects', 'tokenizer_model4'), 'wb'))
