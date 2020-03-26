datapath = "data/train-en-vi/"

with open(datapath+"train.en", 'r', encoding='utf-8') as f:
    linesEN = f.read().split('\n')

with open(datapath+"train.vi", 'r', encoding='utf-8') as f:
    linesVI = f.read().split('\n')

input_texts = []
target_texts = []
input_characters = set()
target_characters = set()
#sample
num_samples = 10000

#
for line in linesEN[: min(num_samples, len(linesEN) - 1)]:
    input_text = line
    input_texts.append(input_text)
    for char in input_text:
        if char not in input_characters:
            input_characters.add(char)

for line in linesVI[: min(num_samples, len(linesVI) - 1)]:
    target_text = '\t' + line + '\n'
    target_texts.append(target_text)
    for char in target_text:
        if char not in target_characters:
            target_characters.add(char)

print(input_texts[155])
print(target_texts[155])
