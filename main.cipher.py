normal_text = "this will be in pig latin"

cipher_text = ""
for word in normal_text.split(" "):
    first_letter = word[0]
    new_word = word.replace(first_letter, "", 1)
    cipher_text = cipher_text + new_word + first_letter + "ay "

print(cipher_text)