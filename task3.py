# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encoding = ""
    prev_char = data[0]
    count = 0
    for i in data:
        if i == prev_char:
            count += 1
        else:
            encoding += str(count) + prev_char
            prev_char = i
            count = 1
    encoding += str(count) + prev_char
    return encoding


def rle_decoding(text):
    decoding = ""
    for i in range(len(text)):
        if str(text[i]).isdigit():
            for j in range(int(text[i])):
                decoding += text[i + 1]
    return decoding

s = 'aaaaaaasssssfgggbbbnnnmm'
print(s)
s_encod = rle_encode(s)
print(s_encod)
s_decod = rle_decoding(s_encod)
print(s_decod)

