alpha = [-1] * 26
text = input()

for index, char in enumerate(text) :
    a_i = ord(char) - ord('a')
    if alpha[a_i] == -1 :
        alpha[a_i] = index
print(' '.join(map(str, alpha)))