tokens =["I", "love", "programming", "in", "Python"]
print("tokens:", tokens)
print("length of the tokens:", len(tokens) )

print("first token:", tokens[0])
print("last token:", tokens[-1])
print("last token:", tokens[len(tokens)-1])

print("first two tokens:", tokens[0:2])
print("Tokens in reverse order :", tokens[::-1])
print("last two tokens:", tokens[-2:])

for token in tokens:
    print(token,end=",")
    
