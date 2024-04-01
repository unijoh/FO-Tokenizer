from tokenizer import tokenize, TOK

text = ("Nógvur vindur verður næstu dagarnar, men fríggjakvøldið minkar vindurin aftur, og síðani verður stilt og meira ella minni turt til annan páskadag tá vindurin vaksur aftur. "
    "Tað veit Veðurstova Føroya.")

for token in tokenize(text):

    print("{0}: '{1}' {2}".format(
        TOK.descr[token.kind],
        token.txt or "-",
        token.val or ""))