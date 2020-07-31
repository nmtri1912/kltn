import re
from nltk import sent_tokenize
from nltk import word_tokenize

f = open('en.txt', 'r', encoding='utf-8')

inp = list(filter(None, f.read().splitlines()))

lenInp = 0
while (True):
    if(lenInp >= len(inp)):
        break
    if(inp[lenInp] == 'report_problem'):
        del(inp[lenInp])
        continue
    lenInp += 1


def pre(w):

    decimal = re.findall(r'\d+[.,\s]\d+', w)
    for i in decimal:
        w = w.replace(i, (re.sub(r'[,.]', "", i)))

    w = w.lower()
    w = re.sub(r'^.{1}\.[\s]*', "", w)
    w = re.sub(r'\s?[^\s]*\.com', "", w)
    w = re.sub(r'[\[\](.*[\)\]]|…', "", w)
    #w = re.sub(r'\(.*?\)|…', "", w)
    w = re.sub(r'n’t|n\'t', " not ", w)
    w = re.sub(r'%', " percent ", w)
    w = re.sub(r'.*\:', "", w)
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r"[:;]", ".", w)
    w = re.sub(r"'re", " are ", w)
    w = re.sub(r"'ve|’ve", " have ", w)
    w = re.sub(r"’[\s]*re", " are ", w)
    w = re.sub(r"'ll ", " will ", w)
    w = re.sub(r"’ll ", " will ", w)
    w = re.sub(r"'m|’m", " am ", w)
    w = re.sub(r"[“”’‘']", "", w)
    w = re.sub(r"[^a-zA-Z0-9?.!,¿]+", " ", w)
    w = re.sub(r" d ", "d ", w)
    w = re.sub(r" s ", "s ", w)
    w = re.sub(r" t ", "t ", w)
    w = re.sub(r'', "", w)
    w = re.sub(r'[" "]+', " ", w)
    w = w.strip()
    return w


def preVn(w):
    w = w.lower()
    decimal = re.findall(r'\d+[.,\s]\d+', w)
    for i in decimal:
        w = w.replace(i, (re.sub(r'[,.]', "", i)))
    w = re.sub(r'^.{1}\.[\s]*', "", w)
    w = re.sub(r'\s?[^\s]*\.com', "", w)
    w = re.sub(r'/', " ", w)
    w = re.sub(r'[\[\](.*[\)\]]|…', "", w)
    #w = re.sub(r'\(.*?\)|…', "", w)
    w = re.sub(r'%', " phần trăm ", w)
    w = re.sub(r'.*\:', "", w)
    w = re.sub(r"[:;]", ".", w)
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r"[“”’‘•']", "", w)
    w = re.sub(r"[–-]+", " , ", w)
    w = re.sub(r'[" "]+', " ", w)
    w = w.strip()
    return w


fe = open('newEn.txt', 'w', encoding='utf-8')
fv = open('newVn.txt', 'w', encoding='utf-8')

f.close()
enOutput = []
vnOutput = []
for i in range(len(inp)):
    if(i % 2 == 0):
        inp[i] = pre(inp[i])
        enOutput.append(sent_tokenize(
            ' '.join(word_tokenize(inp[i], 'english'))))
    else:
        inp[i] = preVn(inp[i])
        vnOutput.append(sent_tokenize(
            ' '.join(word_tokenize(inp[i]))))

for i in enOutput:
    for j in i:
        j = j.strip()
        if(len(j) < 5):
            continue
        if(j[-1] != '.' and j[-1] != '!' and j[-1] != '?'):
            fe.write(j + ' .\n')
        else:
            fe.write(j + '\n')

for i in vnOutput:
    for j in i:
        j = j.strip()
        if(len(j) < 5):
            continue
        if(j[-1] != '.' and j[-1] != '!' and j[-1] != '?'):
            fv.write(j + ' .\n')
        else:
            fv.write(j + '\n')

fe.close()
fv.close()
"""
f = open('en.txt', 'r', encoding='utf-8')

inp = f.read().splitlines()

f.close()

i = 0

while True:
    if(i >= len(inp)):
        break
    inp[i] = inp[i].strip()
    if(inp[i] == '' or inp[i] == ' '):
        del inp[i]
        continue

    elif(len(inp[i]) > 2):
        if(inp[i][0:2] == '>>'):
            del inp[i]
            continue
    i += 1


fe = open('newEn.txt', 'w', encoding='utf-8')
fv = open('newVn.txt', 'w', encoding='utf-8')

lenght = 0

for i in range(len(inp)):
    inp[i] = inp[i].strip()
    inp[i] = inp[i].replace('…', '.')
    inp[i] = inp[i].replace('  ', '')
    inp[i] = inp[i].replace('“', '"')
    inp[i] = inp[i].replace('”', '"')
    inp[i] = inp[i].replace(';', '.')
    inp[i] = inp[i].replace(':', ',')
    inp[i] = inp[i].replace('‘', '\'')
    inp[i] = inp[i].replace('’', '\'')
    inp[i] = inp[i].replace('"', '')
    inp[i] = inp[i].replace('\\', '')
    inp[i] = inp[i].strip()
    temp = inp[i].split('. ')
    for h in range(len(temp)):
        if(temp[h][-1] != '.' and temp[h][-1] != '!' and temp[h][-1] != '?'):
            temp[h] = temp[h] + '.\n'
            lenght += 1
        else:
            temp[h] = temp[h] + '\n'
            lenght += 1
    if(i % 2 == 0):
        fv.writelines(temp)
    else:
        fe.writelines(temp)

print(lenght)
fe.close()
fv.close()

"""

'''

def detachStr(ip):
    # ip = re.sub('"()', '.', ip)

    ip = ip.replace('…', '.')
    ip = ip.replace('\n', '')
    ip = ip.replace('  ', '')
    ip = ip.replace('“', '"')
    ip = ip.replace('”', '"')
    ip = ip.replace(';', '.')
    ip = ip.replace(':', '.')
    ip = ip.replace('‘', '\'')
    ip = ip.replace('’', '\'')
    ip = ip.replace('"', '')
    ip = ip.replace(' *** ', ' ')

    inputArray = []
    index = 0
    temp = 0
    lenInput = len(ip)
    # có phải trong dấu nháy không
    isInApostrophe = False
    # có phải trong dấu ngoặc đơn không
    isParentheses = False
    while index < lenInput - 1:
        if(ip[index] == '"'):
            isInApostrophe = not(isInApostrophe)
        if(ip[index] == '('):
            isParentheses = True
        if(ip[index] == ')'):
            isParentheses = False
        if((ip[index] == '.' or ip[index] == '?' or ip[index] == '!' or ip[index] == ';') and ip[index + 1] == '"'and isInApostrophe == False and isParentheses == False):
            strTemp = ip[temp: index + 2]
            strTemp = strTemp.strip()
            inputArray.append(strTemp)
            temp = index + 2
            index += 2
            continue
        if((ip[index] == '.' or ip[index] == '?' or ip[index] == '!' or ip[index] == ';') and isInApostrophe == False and isParentheses == False):
            strTemp = ip[temp: index + 1]
            strTemp = strTemp.strip()
            inputArray.append(strTemp)
            temp = index + 1
            index += 1
            continue
        # Thêm câu cuối của chuỗi
        if(index == lenInput-2):
            strTemp = ip[temp: index + 2]
            strTemp = strTemp.strip()
            inputArray.append(strTemp)
        index += 1

    return inputArray


en_fb = open('en.txt', 'r', encoding='utf-8')
en_arr = en_fb.readlines()
vn_fb = open('vn.txt', 'r', encoding='utf-8')
vn_arr = vn_fb.readlines()
vn_fb.close()
en_fb.close()
ipen = ''
ipvn = ''

for i in range(len(en_arr)):
    en_arr[i] = re.sub('\n', '', en_arr[i])
    en_arr[i] = en_arr[i].strip()
    if(len(en_arr[i]) > 0):
        if(en_arr[i][-1] != '.'and en_arr[i][-1] != '?'and en_arr[i][-1] != '!'and en_arr[i][-1] != '.' and en_arr[i][-1] != ';'):
            en_arr[i] = en_arr[i] + '.'

for i in range(len(vn_arr)):
    vn_arr[i] = re.sub('\n', '', vn_arr[i])
    vn_arr[i] = vn_arr[i].strip()
    if(len(vn_arr[i]) > 0):
        if(vn_arr[i][-1] != '.'and vn_arr[i][-1] != '?'and vn_arr[i][-1] != '!'and vn_arr[i][-1] != '.' and vn_arr[i][-1] != ';'):
            vn_arr[i] = vn_arr[i] + '.'


ipen = ipen.join(en_arr)
ipenArr = detachStr(ipen)

ipvn = ipvn.join(vn_arr)
ipvnArr = detachStr(ipvn)

en_fb = open('newEn.txt', 'w', encoding='utf-8')
vn_fb = open('newVn.txt', 'w', encoding='utf-8')

for i in ipenArr:
    if(len(i) < 2):
        continue
    if(i[-1] != '.' and i[-1] != '?'and i[-1] != '!'and i[-1] != '.' and i[-1] != ';'):
        en_fb.write(i + '.\n')
    else:
        en_fb.write(i + '\n')


for i in ipvnArr:
    if(len(i) < 2):
        continue
    if(i[-1] != '.'and i[-1] != '?'and i[-1] != '!'and i[-1] != '.' and i[-1] != ';'):
        vn_fb.write(i + '\n')
    else:
        vn_fb.write(i + '\n')

en_fb.close()
vn_fb.close()
print(len(ipenArr))
print(len(ipvnArr))

'''
"""
en_fb = open('en.txt', 'r', encoding='utf-8')
vn_fb = open('vn.txt', 'r', encoding='utf-8')

en_arr = en_fb.readlines()
vn_arr = vn_fb.readlines()
print(en_arr[0])
print(vn_arr[0])

new_en_arr = []
new_vn_arr = []

i = 0
index = 0
temp = 0

while (i < len(en_arr)):
    if(len(en_arr[i]) == 0):
        i += 1
        continue
    en_arr[i] = re.sub('"()', '', en_arr[i])
    lenStr = len(en_arr[i])
    # print(en_arr[i])
    while(index < lenStr):
        if(en_arr[i][index] == '.' or en_arr[i][index] == '?' or en_arr[i][index] == '!'):
            strTemp = en_arr[i][temp:index+1]
            # strTemp = strTemp.strip()
            new_en_arr.append(strTemp)
            temp = index + 1
            index += 1
            continue
        if(index == lenStr - 1):
            strTemp = en_arr[i][temp: index + 1]
            strTemp = strTemp.strip()
            new_en_arr.append(strTemp)
        index += 1
    i += 1

print(len(new_en_arr))

i = 0
index = 0
temp = 0

while (i < len(vn_arr)):
    if(len(vn_arr[i]) == 0):
        i += 1
        continue
    vn_arr[i] = re.sub('"()', '', vn_arr[i])
    lenStr = len(vn_arr[i])
    # print(vn_arr[i])
    while(index < lenStr):
        if(vn_arr[i][index] == '.' or vn_arr[i][index] == '?' or vn_arr[i][index] == '!'):
            strTemp = vn_arr[i][temp:index+1]
            # strTemp = strTemp.strip()
            new_vn_arr.append(strTemp)
            temp = index + 1
            index += 1
            continue
        if(index == lenStr - 1):
            strTemp = vn_arr[i][temp: index + 1]
            strTemp = strTemp.strip()
            new_vn_arr.append(strTemp)
        index += 1
    i += 1

print(len(new_vn_arr))

en_fb.close()
vn_fb.close()
"""
