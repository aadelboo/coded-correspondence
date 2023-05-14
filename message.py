alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10
message_decoded = ""

for letter in message:
    if letter in alphabet:
        letter_pos = alphabet.find(letter)
        real_pos = (letter_pos + offset) % 26
        message_decoded += alphabet[real_pos]
    else:
        message_decoded += letter
print(message_decoded)
