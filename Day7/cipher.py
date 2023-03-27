import module
print(module.art)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define empty global varibale
encrypted_text = None


def encrypt(plain_text, shift_amount):
    e_list = []
    for t in plain_text:
        position = alphabet.index(t)
        # print(position)
        new_position = position+shift_amount
        # print(new_position)
        e_text = alphabet[new_position]
        for e in e_text:
            e_list.append(e)
    # print(e_list)
    global encrypted_text
    encrypted_text = "".join(e_list)
    print(f"Here is the encoded message:\n{encrypted_text}")


def decrypt(e, shift_amount):
    d_list = []
    global encrypted_text
    for t in e:  # here e=encrypted_text which is global variable
        # e_position is encrypted text position comapred to alphabet position
        e_position = alphabet.index(t)
        # d_position is original decrypted position compared to alphabet
        d_position = (e_position - shift_amount) % len(alphabet)
        d_text = alphabet[d_position]
        for d in d_text:
            d_list.append(d)
    decrypted_text = "".join(d_list)
    print(f"Here is the decoded message:\n{decrypted_text}")


# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt or 'q' to quit:\n").lower()
# if condition to decode or encode
while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or 'q' to quit:\n").lower()

    if direction == "q":
        break
    else:
        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(plain_text=text, shift_amount=shift)
        elif direction == "decode":
            encrypted_text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(e=encrypted_text, shift_amount=shift)

    # Ask the user if they want to continue
    repeat = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if repeat != "yes":
        break
