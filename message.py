alphabet = "abcdefghijklmnopqrstuvwxyz"
message_one = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
offset = 14

def decode(message_one, offset):
    message_decoded = ""
    for letter in message_one:
        if letter in alphabet:
            letter_pos = alphabet.find(letter)
            real_pos = (letter_pos + offset) % 26
            message_decoded += alphabet[real_pos]
        else:
            message_decoded += letter
    return message_decoded


print(decode(message_one, offset))

message_two = "performing multiple caesar ciphers to code your messages is even more secure!"
offset = 14
def encode(message_two, offset):
    message_encoded = ""
    for letter in message_two:
        if letter in alphabet:
            letter_pos = alphabet.find(letter)
            real_pos = (letter_pos - offset) % 26
            message_encoded += alphabet[real_pos]
        else:
            message_encoded += letter
    return message_encoded

print(encode(message_two, offset))

brute_force = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
for offset_number in range(1, 26):
    print(encode(brute_force, offset_number))

#############  codecademy solution from here  #####################
def vigenere_decode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for letter in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if letter in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += letter

    message_decoded = ""

    for letter in range(len(message)):
        if message[letter] in alphabet:
            letter_pos = alphabet.find(message[letter])
            keyword_pos = alphabet.find(keyword_phrase[letter])
            real_pos = alphabet[(letter_pos + keyword_pos) % 26]
            message_decoded += real_pos
        else:
            message_decoded += message[letter]

    return message_decoded


message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
keyword = "friends"

print(vigenere_decode(message, keyword))


def vigenere_encode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for letter in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if letter in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += letter

    message_encoded = ""

    for letter in range(len(message)):
        if message[letter] in alphabet:
            letter_pos = alphabet.find(message[letter])
            keyword_pos = alphabet.find(keyword_phrase[letter])
            real_pos = alphabet[(letter_pos - keyword_pos) % 26]
            message_encoded += real_pos
        else:
            message_encoded += message[letter]

    return message_encoded


message_to_encode = "was nott able to build this function on my own. I had to look at the solution. I will try to build it on my own next time."
keyword_to_encode = "focus"

print(vigenere_encode(message_to_encode, keyword_to_encode))
print(vigenere_decode(vigenere_encode(message_to_encode, keyword_to_encode), keyword_to_encode))
