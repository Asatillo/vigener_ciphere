# Vigenère cipher
Method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword.

In a Caesar cipher, each letter of the alphabet is shifted along some number of places. For example, in a Caesar cipher of shift 3, a would become D, b would become E, y would become B and so on. The Vigenère cipher has several Caesar ciphers in sequence with different shift values.

To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square or Vigenère table. It has the alphabet written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar ciphers. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.

![image](https://user-images.githubusercontent.com/35137354/152219943-d2660014-a2a2-4390-a590-9bdb1222a92d.png)

For example, suppose that the plaintext to be encrypted is

> attackatdawn

The person sending the message chooses a keyword and repeats it until it matches the length of the plaintext, for example, the keyword "LEMON":

> LEMONLEMONLE

Each row starts with a key letter. The rest of the row holds the letters A to Z (in shifted order). Although there are 26 key rows shown, a code will use only as many keys (different alphabets) as there are unique letters in the key string, here just 5 keys: {L, E, M, O, N}. For successive letters of the message, successive letters of the key string will be taken and each message letter enciphered by using its corresponding key row. The next letter of the key is chosen, and that row is gone along to find the column heading that matches the message character. The letter at the intersection of [key-row, msg-col] is the enciphered letter.

For example, the first letter of the plaintext, a, is paired with L, the first letter of the key. Therefore, row L and column A of the Vigenère square are used, namely L. Similarly, for the second letter of the plaintext, the second letter of the key is used. The letter at row E and column T is X. The rest of the plaintext is enciphered in a similar fashion:
```
 Plaintext:	attackatdawn
 Key:	        LEMONLEMONLE
 Ciphertext:	LXFOPVEFRNHR
```
Decryption is performed by going to the row in the table corresponding to the key, finding the position of the ciphertext letter in that row and then using the column's label as the plaintext. For example, in row L (from LEMON), the ciphertext L appears in column A, so a is the first plaintext letter. Next, in row E (from LEMON), the ciphertext X is located in column T. Thus t is the second plaintext letter.[Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
