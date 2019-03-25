# coding=utf-8
alphabet = "АБВГҐДЂЃЕЀЁЄЖЗЗ́ЅИЍІЇЙЈКЛЉМНЊОПРСС́ТЋЌУЎФХЦЧЏШЩЪЫЬЭЮЯ"
word = u"млб зрмли анлйэ"
for i in range(26):
    out = [unichr(ord(char)+i) if ord(char) != 32 else unichr(32) for char in word]
    print(''.join(out))
