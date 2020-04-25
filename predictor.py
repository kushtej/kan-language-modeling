from pickle import load
from keras.models import load_model
# from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


def textGenerator(model, tokenizer, seq_len, seed_text, num_gen_words):
    output_text = []
    input_text = seed_text

    for i in range(num_gen_words):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences(
            [encoded_text], maxlen=seq_len, truncating='pre')
        pred_word_ind = model.predict_classes(pad_encoded, verbose=0)[0]

        pre_word = tokenizer.index_word[pred_word_ind]
        input_text += ' ' + pre_word
        output_text.append(pre_word)
    # return ' '.join(output_text)
    return output_text


model = load_model('model.h5')
tokenizer = load(open('tokenizer_model4', 'rb'))
seq_len = 3

print("\n\n===>Enter --exit to exit from the program")
while True:
    num_gen_words = 3
    seed_text = input("Enter String: ")
    if seed_text.lower() == '--exit':
        break
    else:
        out = textGenerator(model, tokenizer, seq_len=seq_len,
                            seed_text=seed_text, num_gen_words=num_gen_words)
        print('output: ' + seed_text)
        print(out)
        print('\n')
