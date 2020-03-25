import numpy as np

# Vocabulary of English
all_eng_words=set()
for eng in lines.eng:
    for word in eng.split():
        if word not in all_eng_words:
            all_eng_words.add(word)

# Vocabulary of VietNamese
all_vi_words=set()
for vi in lines.vi:
    for word in vi.split():
        if word not in all_marathi_words:
            all_vi_words.add(word)


# Max Length of source sequence
lenght_list=[]
for l in lines.eng:
    lenght_list.append(len(l.split(' ')))
max_length_src = np.max(lenght_list)

# Max Length of target sequence
lenght_list=[]
for l in lines.vi:
    lenght_list.append(len(l.split(' ')))
max_length_tar = np.max(lenght_list)