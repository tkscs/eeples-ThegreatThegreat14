original_song = "I like to eat, eat, eat, apples and bananas"

new_song = ""
for character in original_song:
    new_song = new_song + character*3
print(new_song)

print(original_song.replace("a", "aaa"))

new_song = ""
for character in original_song:
    if character == "a":
        new_song = new_song + character*3
    else:
        new_song = new_song + character
print(new_song)

def new_vowel(vowel):
    new_song = original_song.replace("ea", f"{vowel}")
    new_song = new_song.replace("ap", f"{vowel}p")
    new_song = new_song.replace("na", f"n{vowel}")
    print(new_song)
new_vowel("ay")
new_vowel("ee")
new_vowel("i")
new_vowel("o")
new_vowel("u")

# sing("ay")
# sing("ee")
# sing("i")
# sing("o")
# sing("u")

# III   llliiikkkeee   tttooo
# I like to eaaat, eaaat
# I like to eayt, eayt
# I like to eeet, eeet