word = input("Enter a word: ") or "python"

print("The word is:", word)
print("The length of the word is:", len(word))

characters=list(word)
print("The characters in the word are:", characters)

pairs=list(zip(characters, characters[1:]))

print("Adjacent pairs:",pairs)
