#BPE (Byte Pair Encoding) tokenization using pre-trained GPT-2 tokenizer

from transformers import AutoTokenizer 
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = input("Enter a sentence to tokenize:") or "I Love programming in Python"
print("Original sentence:", text)

tokens = tokenizer.tokenize(text)
print(" BPE Tokens:", tokens)

token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("Token IDs:", token_ids)

print("Number of tokens:", len(tokens))

