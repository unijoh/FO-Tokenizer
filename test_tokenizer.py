from fotokenizer.fotokenizer import tokenize, detokenize

# Input text with consecutive whitespaces
input_text = "Hello   world!  This  is  a test."

# Tokenize the input text
tokens = list(tokenize(input_text))

# Print the tokens
print("Tokens:")
for token in tokens:
    print(f"Kind: {token.kind}, Text: '{token.txt}', Original: '{token.original}'")

# Detokenize the tokens back into a string
reconstructed_text = detokenize(tokens)

# Print the reconstructed text
print("\nReconstructed Text:")
print(reconstructed_text)

# Check if the reconstructed text matches the original input
print("\nMatches Original Input:", input_text == reconstructed_text)