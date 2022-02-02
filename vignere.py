
NUM_LETTERS = 26
LETTERS = [chr(i) for i in range(65, 91)]
TABLE = []

for i in range(26):
    TABLE.append([LETTERS[(i + j) % NUM_LETTERS] for j in range(NUM_LETTERS)])


def encrypt(phrase: str, key_word: str):
    phrase = phrase.replace(" ", "").upper()
    key_word = key_word.replace(" ", "").upper()
    len_key_word = len(key_word)
    encrypted = ""
    for i in range(len(phrase)):
        row = ord(phrase[i]) % 65
        column = ord(key_word[i % len_key_word]) % 65
        encrypted += TABLE[row][column]
    return encrypted


def decrypt(phrase: str, key_word: str):
    phrase = phrase.replace(" ", "").upper()
    key_word = key_word.replace(" ", "").upper()
    len_key_word = len(key_word)
    decrypted = ""
    for i in range(len(phrase)):
        column = ord(key_word[i % len_key_word]) % 65
        for j in range(NUM_LETTERS):
            if TABLE[column][j] == phrase[i]:
                decrypted += TABLE[0][j]
    return decrypted