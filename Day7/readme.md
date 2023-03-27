# Caesar Cipher Encoder Decoder

A Caesar cipher is a simple encryption technique in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

In the implementation you provided, the encrypt function takes a plain text and a shift amount as input and then returns the encrypted text by shifting each character of the input text by the specified shift amount.

The decrypt function takes an encrypted text and the shift amount used to encrypt the text as input and then returns the original plain text by shifting each character of the input text in the opposite direction of the shift amount.

The program then takes input from the user to either encode or decode a message using a specified shift amount, and then asks the user if they want to continue or not.

Functions with inputs arguments and parameters are used extensively

```python
def decrypt(e, shift_amount):
d_list = []
global encrypted_text
for t in e: # here e=encrypted_text which is global variable # e_position is encrypted text position comapred to alphabet position
e_position = alphabet.index(t) # d_position is original decrypted position compared to alphabet
d_position = e_position-shift_amount
d_text = alphabet[d_position]
for d in d_text:
d_list.append(d)
decrypted_text = "".join(d_list)
print(f"Here is the decoded message:\n{decrypted_text}")
```
