import re

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
    temp = inp[i].split('. ')
    for h in range(len(temp)):
        temp[h].strip()
        temp[h] = temp[h].replace('…', '.')
        temp[h] = temp[h].replace('  ', '')
        temp[h] = temp[h].replace('“', '"')
        temp[h] = temp[h].replace('”', '"')
        temp[h] = temp[h].replace(';', '.')
        temp[h] = temp[h].replace(':', '.')
        temp[h] = temp[h].replace('‘', '\'')
        temp[h] = temp[h].replace('’', '\'')
        temp[h] = temp[h].replace('"', '')
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

ipen = ipen.join(en_arr)
ipenArr = detachStr(ipen)

ipvn = ipvn.join(vn_arr)
ipvnArr = detachStr(ipvn)

en_fb = open('newEn.txt', 'w', encoding='utf-8')
vn_fb = open('newVn.txt', 'w', encoding='utf-8')

for i in ipenArr:
    en_fb.write(i + '\n')

for i in ipvnArr:
    vn_fb.write(i + '\n')

en_fb.close()
vn_fb.close()
print(len(ipenArr))
print(len(ipvnArr))

"""

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
