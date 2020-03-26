datapath = "data/train-en-vi/"

with open(datapath+"train.en", 'r', encoding='utf-8') as f:
    linesEN = f.read().split('\n')

with open(datapath+"train.vi", 'r', encoding='utf-8') as f:
    linesVI = f.read().split('\n')

input_texts = []
target_texts = []
input_characters = set()
target_characters = set()

input_texts = linesEN