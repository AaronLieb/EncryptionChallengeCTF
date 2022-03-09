# This is a cryptography challenge. Use the output of the program to find "ptxt". The variable "key" is not readable meaning it's consist of random characters. However, "ptxt" is readable meaning it is an English sentence.

# encrypt.py
from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt

#with open('flag.txt') as f, open('key.txt') as k:
#    flag = f.read().strip()
#    key = k.read().strip()

#ptxt = flag[5:-1]

# ctxt = encrypt(ptxt,key)
# pseudo_key = encrypt(key,key)

#print('Ciphertext:',ctxt)
#print('Pseudo-key:',pseudo_key)

# output:
encrypted_text = 'c_ubrgl_zwcokc_xsrs_epy_dzriwo_wcwbfl'
pkey = 'oocoacmauiw'

# 2x % 26 == y
# 2x - y
# x = y/2
# 2x - 26 - y
# x = (y + 26)/2

possible_keys = []

def generate_keys(ckey):
    n = len(ckey)
    if n == len(pkey):
        possible_keys.append(ckey)
        return
    pn = chr_to_num[pkey[n - 1]]
    generate_keys(ckey + num_to_chr[pn/2])
    generate_keys(ckey + num_to_chr[(pn + 26)/2])

generate_keys("")

for k in possible_keys:
    decrypted_text = ""
    k2 = ''.join(k[i % len(k)] for i in range(len(encrypted_text))).lower()
    for i in range(len(encrypted_text)):
        if encrypted_text[i] == "_":
            decrypted_text += "_"
            continue
        n = chr_to_num[encrypted_text[i]]
        y = chr_to_num[k2[i]]
        if y > n:
            decrypted_text += num_to_chr[n - y + 26]
        else:
            decrypted_text += num_to_chr[n - y]

    print(decrypted_text)



        









