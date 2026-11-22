text = input("Enter a sentence : ") or "I love programming in Python"

print("length of the text:", len(text) )
print("characters in the given text are :")

for ch in text:
    print(ch, end=",")
